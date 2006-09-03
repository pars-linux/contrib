#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Uğur Çetin <jnmbk@users.sourceforge.net>

from pisi.actionsapi import scons
from pisi.actionsapi import pisitools

def setup():
    pass

def build():
    scons.make()

def install():
    scons.install()
    pisitools.domove("/bin", "/usr/")
    pisitools.domove("/share", "/usr/")
    pisitools.dodoc("doc/*")