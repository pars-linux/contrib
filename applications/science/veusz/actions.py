#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def install():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.insinto("/usr/share/veusz/examples", "examples/*")
    pisitools.insinto("/usr/share/pixmaps", "images/icon.png", "veusz.png")
    pisitools.insinto("usr/share/applications", "veusz.desktop")

    pisitools.dodoc("AUTHORS", "ChangeLog", "INSTALL", "NEWS", "README", "Documents/*.txt", "Documents/*.pdf")
    pisitools.dohtml("Documents/*")
    pisitools.domove("/usr/share/doc/%s/html/*.png" % get.srcTAG(), "/usr/share/doc/%s/html/manimages" % get.srcTAG())
