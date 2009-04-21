#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def install():
    pisitools.insinto("/usr/bin", "src/kpaste")
    pisitools.insinto("/usr/share/pixmaps", "src/kpaste.png")
    pisitools.insinto("%s/share/apps/konqueror/servicemenus" % get.kdeDIR(), "src/kpaste.desktop")

    pisitools.dodoc("AUTHORS", "README")
