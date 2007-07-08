#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "kim"
appFiles = ["COPYING", "src/slideshow", "src/galery"]

def install():
    pisitools.insinto("/usr/bin", "src/bin/kim*")
    pisitools.insinto("%s/share/apps/konqueror/servicemenus" % get.kdeDIR(), "src/kim*.desktop")
    for file in appFiles:
        pisitools.insinto("%s/share/apps/kim" % get.kdeDIR(), file)
    pisitools.rename("%s/share/apps/kim/COPYING" % get.kdeDIR(), "kim_about.txt")
    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "manual.html")

