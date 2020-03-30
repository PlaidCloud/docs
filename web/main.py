#!/usr/bin/env python
# coding=utf-8

import logging
import os
import tornado.httpserver
import tornado.ioloop
import tornado.web as web
from tornado.options import options, parse_command_line

__author__ = "Kellen Kapper"
__copyright__ = "© Copyright 2018-2019, Tartan Solutions, Inc"
__credits__ = ["Kellen Kapper", "Garrett Bates", "Paul Morel"]
__license__ = "Proprietary"
__maintainer__ = "Kellen Kapper"
__email__ = "kellen.kapper@tartansolutions.com"

# Application Configuration Settings
HANDLER_MAP = [
    (r"/docs/(.*)", web.StaticFileHandler, {
        "path": "/web/docs",
        "default_filename": "index.html",
    })
]

TORNADO_SETTINGS = {
    'debug': False,
}

tornado.options.define("port", default=8000, type=int)
logging.info("Creating Tornado Application")
application = tornado.web.Application(HANDLER_MAP, **TORNADO_SETTINGS)

if __name__ == "__main__":
    try:
        parse_command_line()
        http_server = tornado.httpserver.HTTPServer(application, xheaders=True)
        http_server.listen(options.port)
        logging.info('Tornado listening on port {} with PID {}'.format(options.port, os.getpid()))
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        pass
    except:
        import traceback
        logging.error(traceback.format_exc())
        raise

