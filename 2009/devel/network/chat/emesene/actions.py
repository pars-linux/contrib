#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

share = "/usr/share/emesene"
remove_dirs = ["misc", "libmimic"]
remove_files = ["setup.py", "PKG-INFO"]
move_files = ["LGPL", "PSF", "COPYING", "GPL", "README"]

def install():
    pisitools.insinto("/usr/share/applications", "misc/emesene.desktop")
    pisitools.insinto("/usr/share/pixmaps", "emesene-logo.png", "emesene.png")
    pisitools.insinto("/usr/share/emesene", "*")

    for f in move_files:
        pisitools.domove("%s/%s" % (share, f), "%s/%s" % (get.docDIR(), get.srcNAME()))

    for d in remove_dirs:
        pisitools.removeDir("%s/%s" % (share, d))
    for f in remove_files:
        pisitools.remove("%s/%s" % (share, f))
