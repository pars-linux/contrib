#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

WorkDir = get.srcNAME()
items = ["beryl-core", "beryl-plugins", "beryl-settings", "beryl-manager", "emerald", 
"emerald-themes"]

def setup():
    pisitools.dosed("emerald/misc/Makefile.am", "gnome", "Tulliana-2.0")
    for item in items:
        shelltools.cd(item)
        shelltools.system("./autogen.sh --prefix=/usr")
        shelltools.cd("..")

def build():
    for item in items:
        shelltools.cd(item)
        autotools.make()
        shelltools.cd("..")

def install():
    for item in items:
        shelltools.cd(item)
        autotools.install()
        shelltools.cd("..")
