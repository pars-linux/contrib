#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = ""

def install():
    pisitools.insinto("/opt/MilkyTracker_linux_x86_2006_08_27",  "*")
    pisitools.dosym("/opt/MilkyTracker_linux_x86_2006_08_27/milkytracker.linux-x86",  "/usr/bin/milkytracker")