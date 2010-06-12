#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "FreeRapid-%su1" % get.srcVERSION()

def fixperms(d):
    import os

    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)

        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def install():
    pisitools.insinto("/usr/share/freerapid", "./*")
    fixperms(get.installDIR())

    shelltools.chmod("%s/usr/share/freerapid/frd.sh" % get.installDIR())
    pisitools.dosym("/usr/share/freerapid/frd.sh", "/usr/bin/freerapid")
    pisitools.dosym("/usr/share/freerapid/frd.png", "/usr/share/pixmaps/freerapid.png")

    pisitools.remove("/usr/share/freerapid/frd.exe")
    pisitools.remove("/usr/share/freerapid/tools/nircmd/nircmd.exe")
    pisitools.removeDir("/usr/share/freerapid/tools/gocr")
    pisitools.removeDir("/usr/share/freerapid/doc")

    pisitools.dodoc("doc/*", "License")
