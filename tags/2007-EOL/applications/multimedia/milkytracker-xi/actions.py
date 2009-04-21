#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

WorkDir = "."

def install():
    shelltools.system('unrar x Xi_instruments.rar')

    pisitools.insinto("/opt/MilkyTracker/XI-instruments",  "instrumentos/*")
