#!/usr/bin/env python
# encoding: utf8

from convert import *
from program import *


__version__ = (1, 2, 'dev')


def get_version():
    return ".".join(map(str, __version__))