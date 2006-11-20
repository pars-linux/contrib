#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "pardus-tt"

def install():
    pisitools.dodir("/usr/share/icons/pardus-tt")

    for dir in ("128x128", "96x96", "72x72", "64x64", "48x48", "32x32", "22x22", "16x16", "OTHER"):
        shelltools.copytree(dir, "%s/usr/share/icons/pardus-tt/%s" % (get.installDIR(), dir))

    pisitools.insinto("/usr/share/icons/pardus-tt", "author")
    pisitools.insinto("/usr/share/icons/pardus-tt", "index.desktop")
    pisitools.insinto("/usr/share/icons/pardus-tt", "license.txt")
    pisitools.insinto("/usr/share/icons/pardus-tt", "readme.txt")
    pisitools.insinto("/usr/share/icons/pardus-tt", "thanks.to")