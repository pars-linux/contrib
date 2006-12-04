#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

WorkDir = "cdi2iso"

def setup():
    pass
    

def build():
    autotools.make()
#   shelltools.system("%s src/cdi2iso.c -o %s %s %s" % (get.CC(), get.srcNAME(), get.CFLAGS(), get.LDFLAGS()))

def install():
    pisitools.dobin("cdi2iso")
    pisitools.dodoc("CHANGELOG", "gpl.txt")
