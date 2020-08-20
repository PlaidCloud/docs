#!/usr/bin/env python
# coding=utf-8

import logging
import os

import uvicorn
from starlette.applications import Starlette
from starlette.responses import Response
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles

__author__ = 'Paul Morel'
__maintainer__ = 'Paul Morel <paul.morel@tartansolutions.com>'
__copyright__ = '© Copyright 2020, Tartan Solutions, Inc'
__license__ = "Proprietary"
__maintainer__ = "Garrett Bates"
__email__ = "garrett.bates@tartansolutions.com"

ROOT_PATH = '/web/docs'
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")

logging.basicConfig(
    level=LOG_LEVEL,
    format='%(asctime)s.%(msecs)03d %(levelname)s [%(module)s.%(funcName)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d,%H:%M:%S')

LOGGER = logging.getLogger(__name__)

# -- STANDARD KUBERNETES CHECK ROUTES --
async def readiness_probe(request):
    """Kubernetes pod readiness check endpoint"""
    return Response('ok', status_code=200)

async def liveness_probe(request):
    """Kubernetes pod liveness check endpoint"""
    return Response('ok', status_code=200)

# -- APP SPECIFIC ROUTES --
STATIC_FILES = StaticFiles(directory=ROOT_PATH, html=True)

ROUTES = [
    Route('/ready/', readiness_probe),
    Route('/live/', liveness_probe),
    Mount('/', STATIC_FILES)
]

APP = Starlette(routes=ROUTES, debug=False)


if __name__ == "__main__":
    # This implementation is adapted from an example at:
    # https://www.mattlayman.com/blog/2019/starlette-mock-service/

    try:
        uvicorn.run(APP, host="0.0.0.0", port=8000)
    except KeyboardInterrupt:
        pass
    except:
        import traceback
        LOGGER.error(traceback.format_exc())
        raise

    LOGGER.info('Gracefully exiting')
