#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Uğur Çetin <jnmbk@users.sourceforge.net>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    pass

def build():
    autotools.make("x11")

def install():
    pisitools.dolib_a("lib/x11/libglfw.a")
    pisitools.insinto("/usr/include/GL/", "include/GL/glfw.h")
    pisitools.dohtml("readme.html")
    pisitools.dodoc("docs/*")