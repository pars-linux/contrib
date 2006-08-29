#!/usr/bin/python
#-*- coding: UTF-8 -*-
#
# Uğur Çetin
# jnmbk@users.sourceforge.net

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    shelltools.export("CFLAGS", "%s -I/usr/include/lcms" % get.CFLAGS())
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.removeDir("/var")