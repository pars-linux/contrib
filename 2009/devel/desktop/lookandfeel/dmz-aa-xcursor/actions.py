#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2007-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "Vanilla-DMZ-AA"

def install():
    pisitools.insinto("/usr/share/icons/DMZ-AA", "cursors")
    pisitools.insinto("/usr/share/icons/DMZ-AA", "index.theme")
    pisitools.dodoc("COPYING")
