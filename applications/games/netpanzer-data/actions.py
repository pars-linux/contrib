#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

NoStrip = "/"

import os

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def setup():
    autotools.configure("--disable-sdltest")

def build():
    shelltools.system("jam")

def install():
    shelltools.system("jam -sDESTDIR=%s install" % get.installDIR())

    pisitools.dodoc("ChangeLog", "COPYING", "README", "RELNOTES", "TODO")

    for d in ["cache", "maps", "pics", "powerups", "sound", "units", "wads"]:
        fixperms("%s/usr/share/netpanzer/%s" % (get.installDIR(), d))
