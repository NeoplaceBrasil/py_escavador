# flake8: noqa
from __future__ import absolute_import

VERSION = (0, 0, 1)
__version__ = VERSION
__versionstr__ = ".".join(map(str, VERSION))

import logging

try:  # Python 2.7+
    from logging import NullHandler
except ImportError:

    class NullHandler(logging.Handler):
        def emit(self, record):
            pass


import sys

logger = logging.getLogger("py_escavador")
logger.addHandler(logging.NullHandler())
