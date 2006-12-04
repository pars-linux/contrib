#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pass

def build():
    shelltools.system("%s %s -o %s %s.c" % (get.CC(), get.CFLAGS(), get.srcNAME(), get.srcNAME()))

def install():
    pisitools.dobin("bchunk")
    pisitools.doman("bchunk.1")
    pisitools.dodoc("bchunk-1.2.0.lsm", "README", "ChangeLog", "bchunk.spec")
