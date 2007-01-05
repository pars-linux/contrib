#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "trigger-0.5.2.1-src"

def setup():
    autotools.configure("--disable-sdltest \
                         --with-sdl \
                         --with-libSDL_image \
                         --with-libAlut=/usr/lib \
                         --with-libPhysFS=/usr/lib \
                         --with-x \
                         --datadir=/usr/share/trigger")

def build():
    shelltools.system("jam -qa")

def install():
    pisitools.dobin("trigger")
    pisitools.dodoc("doc/COPYING", "doc/*.txt")
