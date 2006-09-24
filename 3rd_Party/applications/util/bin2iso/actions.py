#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "bin2iso"

def setup():
    pass

def build():
#   shelltools.system("gcc -o bin2iso bin2iso19b_linux.c")
    shelltools.system("%s bin2iso19b_linux.c -o %s %s %s" % (get.CC(), get.srcNAME(), get.CFLAGS(), get.LDFLAGS()))

def install():
    pisitools.dobin("bin2iso")
    pisitools.dodoc("readme.txt")
