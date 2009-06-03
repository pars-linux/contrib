#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "kim"
appFiles = ["src/slideshow", "src/galery"]

def install():
    pisitools.insinto("/usr/bin", "src/bin/kim*")
    pisitools.insinto("%s/share/apps/konqueror/servicemenus" % get.kdeDIR(), "src/kim*.desktop")
    for file in appFiles:
        pisitools.insinto("%s/share/apps/kim" % get.kdeDIR(), file)

    pisitools.dodoc("AUTHORS", "ChangeLog", "README", "COPYING")
