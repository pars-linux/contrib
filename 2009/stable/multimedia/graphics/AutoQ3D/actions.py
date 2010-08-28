#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

datadir = "/usr/share/AutoQ3D-Community"

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

WorkDir = "AutoQ3DCommunity1-40qt4source"

def setup():
    shelltools.system("qmake-qt4")

def build():
    autotools.make()

def install():
    pisitools.dobin("AutoQ3D")
    pisitools.insinto("/usr/share/pixmaps", "AutoQ3D.png")
    pisitools.insinto(datadir, "images")
    pisitools.insinto(datadir, "*.qm")
    pisitools.insinto(datadir, "*.htm")

    #fix directory and file permissions
    fixperms("%s/%s" % (get.installDIR(),datadir))

    pisitools.dodoc("docs/*.txt")


