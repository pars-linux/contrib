#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="Emerald-2.0"

def install():
    pisitools.insinto("/usr/share/amsn/skins/Emerald-2.0", "*")