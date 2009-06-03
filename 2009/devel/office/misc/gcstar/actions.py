#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="%s" % get.srcNAME()

def install():
    shelltools.system("./install --prefix=%s/usr --noclean --nomenu" % get.installDIR())

    pisitools.insinto("/usr/share/applications", "share/applications/gcstar.desktop")
    pisitools.insinto("/usr/share/pixmaps", "share/gcstar/icons/gcstar_64x64.png", "gcstar.png")
    pisitools.insinto("/usr/share/mime/packages", "share/applications/gcstar.xml")

    pisitools.dodoc("CHANGELOG", "README", "LICENSE")
