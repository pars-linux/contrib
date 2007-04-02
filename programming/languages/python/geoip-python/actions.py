#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules

WorkDir="GeoIP-Python-1.2.1"

def install():
    pythonmodules.install()

    pisitools.dodoc("ChangeLog","README")
