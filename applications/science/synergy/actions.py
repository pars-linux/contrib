#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools

WorkDir = "weber"
NoStrip = "/"

def install():
    pisitools.insinto("/usr/weber", "*")
    pisitools.insinto("/usr/share/applications", "Synergy.desktop")
    pisitools.dosym("/usr/weber/bin/synergy", "/usr/bin/synergy")

