"""
    setup
    ~~~~
    SQLRaw is a simple extension for Python that allows us access to all
    SQL commands as string capabilities with change it with format
    function in Python.

    :copyright: (c) 2024 by Shahriyar Tarnasi.
    :license: MIT, see LICENSE for more details.
"""

from .version import __version__

# Set default logging handler to avoid "No handler found" warnings.
import logging
from logging import NullHandler

# Set initial level to WARN. Users must manually enable logging for
# flask_cors to see our logging.
rootlogger = logging.getLogger(__name__)
rootlogger.addHandler(NullHandler())

if rootlogger.level == logging.NOTSET:
    rootlogger.setLevel(logging.WARN)
