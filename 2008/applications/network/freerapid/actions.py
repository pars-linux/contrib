#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir = "FreeRapid-%s" % get.srcVERSION()

def setup():
    pisitools.dodir("%s/usr/share/freerapid" % get.installDIR())
    pisitools.dodir("%s/usr/share/pixmaps/" % get.installDIR())

def install():
    shelltools.copytree("lib/", "%s/usr/share/freerapid/" % get.installDIR())
    shelltools.copytree("lookandfeel/", "%s/usr/share/freerapid/" % get.installDIR())
    shelltools.copytree("plugins/", "%s/usr/share/freerapid/" % get.installDIR())
    shelltools.copytree("tools/", "%s/usr/share/freerapid/" % get.installDIR())

    pisitools.dobin("frd.sh", "/usr/share/freerapid")

    pisitools.insinto("/usr/share/pixmaps/", "frd.png")
    shelltools.copy("*", "%s/usr/share/freerapid/" % get.installDIR())

    pisitools.remove("/usr/share/freerapid/frd.exe")
    pisitools.remove("/usr/share/freerapid/readme*txt")

    shelltools.system("chmod +x %s/usr/share/freerapid/frd.sh" % get.installDIR())

    pisitools.dosym("/usr/share/freerapid/frd.sh", "/usr/bin/freerapid") 
