#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "AutoQ3Dsource"

def setup():
    shelltools.system("qmake-qt4")

def build():
    autotools.make()

def install():
    pisitools.dobin("AutoQ3D")

    shelltools.chmod("*.qm", 0644)
    shelltools.chmod("*.png", 0644)
    shelltools.chmod("images/*", 0644)

    pisitools.insinto("/usr/share/AutoQ3D", "images")
    pisitools.insinto("/usr/share/AutoQ3D", "*.qm")

    pisitools.insinto("/usr/share/pixmaps", "AutoQ3D.png")
    pisitools.dodoc("docs/*")
