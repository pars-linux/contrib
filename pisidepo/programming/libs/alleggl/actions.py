#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# by Serkan Avci <killer@wolke7.net>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "alleggl"

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()