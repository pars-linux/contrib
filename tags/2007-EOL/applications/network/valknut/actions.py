#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--with-qt-dir=/usr/qt/3 \
                         --disable-xmltest \
                         --disable-link-static \
                         --enable-lfs")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.insinto("/usr/share/pixmaps", "valknut/icons/icon_22x22.png")
    pisitools.rename("/usr/share/pixmaps/icon_22x22.png" , "valknut.png")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
