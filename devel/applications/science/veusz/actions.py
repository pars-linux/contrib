#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def install():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.insinto("/usr/share/veusz/examples", "examples/*")
    pisitools.insinto("/usr/share/pixmaps", "windows/icons/veusz.png")
    pisitools.insinto("usr/share/applications", "veusz.desktop")

    pisitools.dohtml("Documents/*")
    pisitools.domove("/usr/share/doc/%s/html/*.png" % get.srcTAG(), "/usr/share/doc/%s/html/manimages" % get.srcTAG())
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "VERSION", "Documents/*.txt", "Documents/*.pdf")
