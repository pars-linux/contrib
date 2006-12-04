#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

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