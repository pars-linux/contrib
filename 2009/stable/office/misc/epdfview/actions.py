#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("data/epdfview.desktop",
                    "Icon=icon_epdfview-48",
                    "Icon=epdfview")

    autotools.configure("--disable-rpath")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dosym("/usr/share/epdfview/pixmaps/icon_epdfview-48.png",
                    "/usr/share/pixmaps/epdfview.png")

    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "COPYING", "NEWS", "README", "THANKS")
