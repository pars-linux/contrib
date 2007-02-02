#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

def setup():
    autotools.configure("--prefix=/usr \
                         --exec-prefix=/usr \
                         --enable-threadsafe \
                         --enable-debug \
                         --enable-release")

    #-ljpeg -lpng -ltiff -lz -lbz2 -lGL -lGLU \
    #--disable-jpeg --disable-png --disable-tiff --disable-zlib --disable-bz2lib
    #--disable-static --disable-shared --with-xcursor=no --with-xft=yes
    #--with-opengl=no

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("ADDITIONS", "AUTHORS", "INSTALL", "LICENSE*", "README", "TRACING")
