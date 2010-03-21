#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools

WorkDir = "kicad"

def setup():
    cmaketools.configure(sourceDir=".")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/pixmaps", "bitmaps/icon_eeschema.xpm", "eeschema.xpm")

    pisitools.dodoc("AUTHORS.txt", "CHANGELOG*", "COPYRIGHT.txt", "TODO.txt", "version.txt")
