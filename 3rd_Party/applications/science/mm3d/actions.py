#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("src/libmm3d/mm3dconfig.h", "(/share/doc/)mm3d/", r"\1%s/" % get.srcTAG())
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.insinto("/usr/share/icons/hicolor/16x16/apps", "src/pixmap/mm3dlogo-16x16.xpm", "mm3d.xpm")
    pisitools.insinto("/usr/share/icons/hicolor/32x32/apps", "src/pixmap/mm3dlogo-32x32.xpm", "mm3d.xpm")

    pisitools.rename("/usr/share/doc/mm3d", get.srcTAG())
    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "README*", "NEWS", "TODO")
