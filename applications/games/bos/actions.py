#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "."
NoStrip = "/"

def install():
    pisitools.dodir("/usr/share/bos")

    shelltools.copytree("data.bos", "%s/usr/share/bos" % get.installDIR())

    pisitools.dodoc("data.bos/*.txt", "data.bos/CHANGELOG")

    # Remove duplicate doc files
    pisitools.remove("/usr/share/bos/data.bos/*.txt")
    pisitools.remove("/usr/share/bos/data.bos/CHANGELOG")