#!/usr/bin/env python
# coding=utf-8

import sys
import signal
import multiprocessing
from multiprocessing import pool
import os

import tornado.httpserver
import tornado.ioloop
import tornado.web

from plaid.core import config
from plaid.core.utility import plogging
from plaid.web.handlers import ui

__author__ = "Paul Morel"
__copyright__ = "© Copyright 2018, Tartan Solutions, Inc"
__credits__ = ["Paul Morel"]
__license__ = "Proprietary"
__maintainer__ = "Paul Morel"
__email__ = "paul.morel@tartansolutions.com"

PLAID_CONFIG = config.get_dict()

# Application Configuration Settings
HANDLER_MAP = [
    (r"/(.*)", tornado.web.StaticFileHandler, {"path": "/home/plaid/src/docs/build"}),
]

# No cookie or session handling required for static docs access
TORNADO_SETTINGS = {}


def sigterm_callback(*args, **kwargs):
    tornado.ioloop.IOLoop.instance().stop()


def sigterm_handler(signum, frame):
    # turn off our signal handlers
    signal.signal(signal.SIGTERM, signal.SIG_DFL)
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    # generate log message
    signame = "???"
    if signum == signal.SIGINT:
        signame = "SIGINT"
    elif signum == signal.SIGTERM:
        signame = "SIGTERM"

    logger.info("Caught %s, stopping IOLoop..." % signame)
    tornado.ioloop.IOLoop.instance().add_callback_from_signal(sigterm_callback)


logger = plogging.get_logger_adapter('plaid.web.main', '127.0.0.1', 'DAEMON')


class NDProcess(multiprocessing.Process):
    """ A non-daemonic process for use with NDPool """
    def _get_daemon(self):
        return False

    def _set_daemon(self, value):
        pass

    daemon = property(_get_daemon, _set_daemon)


class NDPool(pool.Pool):
    """ A Non-daemonic process pool """
    Process = NDProcess


def launch_tornado(port=8000):
    """ Launches a tornado processes on the given port.

    This should be used in conjunction with a multiprocessing pool as a manual
    implementation of Tornado's multiprocessing, as Tornado's
    implemantation always listens on the same port. This allows for each process
    to listen on a different port.

    @param port: The port to have Tornado listen on.
    """
    application = tornado.web.Application(HANDLER_MAP, **TORNADO_SETTINGS)
    http_server = tornado.httpserver.HTTPServer(application, xheaders=True)
    http_server.listen(port)
    # Set up signal handlers to exit gracefully when the server is stopped.
    signal.signal(signal.SIGTERM, sigterm_handler)  # killed
    signal.signal(signal.SIGINT, sigterm_handler)  # ctrl+c
    logger.info('Tornado listening on port {} with PID {}'.format(port, os.getpid()))
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    # Grab the number of cores on the machine.
    # This is done to manually launch Tornado in
    # Multiprocessing mode. Tornado's built-in
    # Implementation doesn't allow for listening
    # on multiple ports.
    core_count = multiprocessing.cpu_count()
    servers = []

    try:
        port = int(sys.argv[1])
    except:
        port = 8000  # Plaid Server Port

    if sys.argv[-1] == "--profiling":
        TORNADO_SETTINGS['profiling'] = True
        logger.warning("Profiling mode enabled, performance will suck!")
    else:
        TORNADO_SETTINGS['profiling'] = False

    # Manually creating these processes so that they listen on different ports.
    try:
        # Assume that we should listen on ports 8000-(8000 + number of cores in the machine)
        # Note that Nginx should be configured to load balance between those ports.
        ports = [p for p in range(port, port+core_count)]
        # Have to use a Non-Daemonic pool for Tornado since the UI handler creates its
        # own pool. Python doesn't allow daemonic pools in daemonic pools.
        tornado_pool = NDPool(core_count)
        tornado_pool.map(launch_tornado, ports)
    except:
        import traceback
        logger.error(traceback.format_exc())
        raise
    logger.info('Tornado launched')
    # tornado.ioloop.IOLoop.instance().start()

    # When IOLoop.stop() is called, we eventually reach this code
    if ui.UIHandler.ui_pool is not None:
        logger.info("Killing our kids")
        ui.UIHandler.ui_pool.close()
        ui.UIHandler.ui_pool.join()
    logger.info("Gracefully exiting")
