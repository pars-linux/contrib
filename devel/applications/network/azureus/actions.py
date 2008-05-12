#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006,2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

WorkDir = "azureus"

def setup():
    pisitools.dosed('azureus', 'JAVA_PROGRAM_DIR=""', 'JAVA_PROGRAM_DIR="/opt/sun-jre/bin/"')
    pisitools.dosed('azureus', '#PROGRAM_DIR="/home/username/apps/azureus"', 'PROGRAM_DIR="/usr/share/azureus"')

def install():
    pisitools.insinto("/usr/share/azureus", "*")
    pisitools.insinto("/usr/share/pixmaps/", "Azureus.png")

    pisitools.dosym("/usr/share/azureus/azureus", "/usr/bin/azureus")
