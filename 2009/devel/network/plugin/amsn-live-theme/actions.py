#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="aMSN Live-1.0"

def install():
    pisitools.insinto("/usr/share/amsn/skins/aMSN Live-1.0", "*") 
