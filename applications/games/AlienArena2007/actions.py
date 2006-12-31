#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="alienarena2007"

def install():
    pisitools.insinto("/opt/alienarena2007", "*")
    pisitools.dodoc("README.txt")
    pisitools.dosym("/opt/alienarena2007/AlienArena", "/usr/bin/AlienArena")