#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

def install():
    pisitools.insinto("/usr/bin", "src/kpaste")
    pisitools.insinto("/usr/share/pixmaps", "src/kpaste.png")
    pisitools.insinto("/usr/kde/3.5/share/apps/konqueror/servicemenus", "src/kpaste.desktop")
    pisitools.dodoc("AUTHORS", "README")