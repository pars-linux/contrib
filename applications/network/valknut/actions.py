#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-xmltest \
                         --disable-link-static \
                         --enable-lfs")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.insinto("/usr/share/pixmaps", "valknut/icons/icon_22x22.png")
    pisitools.rename("/usr/share/pixmaps/icon_22x22.png" , "valknut.png")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "INSTALL", "NEWS", "README")
