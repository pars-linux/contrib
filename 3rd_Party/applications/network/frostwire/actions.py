#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "FrostWire-4.10.9"
NoStrip = "/"

def setup():
    pass

def build():
    pass

def install():
    pisitools.insinto("/usr/lib/", "usr/lib/*")
    pisitools.insinto("/usr/share/", "usr/share/*")
    pisitools.doexe("usr/bin/frostwire", "/usr/bin")