#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

WorkDir = "."

def install():
    shelltools.system('unrar x Xi_instruments.rar')

    pisitools.insinto("/opt/MilkyTracker_linux_x86_2006_08_27/XI - instruments",  "instrumentos/*")
