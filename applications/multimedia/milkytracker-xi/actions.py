#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "."

def install():
    shelltools.system('unrar x XI%20-%20instruments.rar')
    pisitools.insinto("/opt/MilkyTracker_linux_x86_2006_08_27/XI - instruments",  "instrumentos/*")
