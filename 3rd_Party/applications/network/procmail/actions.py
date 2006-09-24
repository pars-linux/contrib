#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile", "CFLAGS0 = -O", "CFLAGS0 = " + get.CFLAGS())
    pisitools.dosed("Makefile", "LOCKINGTEST=__defaults__", "#LOCKINGTEST=__defaults__")
    pisitools.dosed("Makefile", "#LOCKINGTEST=/tmp", "LOCKINGTEST=/tmp")
    pisitools.dosed("src/authenticate.c", "/\*#define MAILSPOOLHOME \"/.mail\"", "#define MAILSPOOLHOME \"/.maildir/\"")

def build():
    autotools.make()

def install():
    pisitools.dobin("new/procmail")
    pisitools.dobin("new/lockfile")
    pisitools.dobin("new/formail")
    pisitools.dobin("new/mailstat")
    pisitools.doman("*.1")
    pisitools.doman("*.5")
    pisitools.dodoc("Artistic", "COPYING", "FAQ", "FEATURES", "HISTORY", "INSTALL", "KNOWN_BUGS", "README")
    pisitools.dodir("/usr/share/doc/%s/examples" % get.srcTAG())
    pisitools.insinto("/usr/share/doc/%s/examples" % get.srcTAG(), "examples/*")
