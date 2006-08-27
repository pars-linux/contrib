#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.autoconf()
#   shelltools.export("append-flags", "-I/usr/include/db1")
    shelltools.export("CFLAGS", "%s -I/usr/include/db1" % get.CFLAGS())
    shelltools.export("ESD_CONFIG", "no")
    autotools.rawConfigure("--disable-nls \
                            --with-kde-datadir=%s/share \
                            --disable-gtk-doc \
                            --enable-prefer-db1" % get.kdeDIR())

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "ChangeLog", "COPYING*", "INSTALL", "NEWS", "README", "TODO")
