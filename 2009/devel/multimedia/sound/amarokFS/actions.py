#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
import os

def setup():
    shelltools.system("qmake amarokFS-xml.pro")
    pisitools.dosed("Makefile", ".*strip.*")

def build():
    autotools.make()

def install():
    pisitools.chmod("amarokFS.png", 644)
    for root, dirs, files in os.walk('images'):
        for file in files:
            pisitools.chmod(pisitools.join_path(root, file), 644)

    pisitools.dobin("amarokFS", "/usr/bin")

    pisitools.insinto("/usr/share/amarokFS", "theme.xml")
    pisitools.insinto("/usr/share/icons", "amarokFS.png")
    pisitools.insinto("/usr/share/applications", "amarokFS.desktop")
    pisitools.insinto("/usr/share/amarokFS/images", "images/*")

    pisitools.dodoc("README", "theme-howto.txt")
