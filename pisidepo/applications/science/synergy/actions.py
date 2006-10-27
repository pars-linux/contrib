#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "weber"
NoStrip = "/"

def install():
    pisitools.insinto("/usr/weber", "*")
    pisitools.insinto("/usr/share/applications", "Synergy.desktop")
    pisitools.dosym("/usr/weber/bin/synergy", "/usr/bin/synergy")