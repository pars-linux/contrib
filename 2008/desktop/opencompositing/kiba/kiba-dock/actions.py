#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools

def setup():
    libtools.libtoolize()
    shelltools.system("./autogen.sh")
    autotools.configure("--disable-static \
                         --disable-glitz \
                         --enable-akamaru \
                         --enable-svg \
                         --disable-sdl")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING")
