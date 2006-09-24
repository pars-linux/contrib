#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "b5i2iso-0.2-src"

def setup():
    pass

def build():
    shelltools.system("%s src/%s.c -o %s %s" % (get.CC(), get.srcNAME(), get.srcNAME(), get.CFLAGS()))

def install():
    pisitools.dobin("b5i2iso")
    pisitools.dodoc("CHANGELOG", "gpl.txt")
