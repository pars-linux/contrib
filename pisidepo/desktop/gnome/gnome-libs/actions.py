#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    autotools.autoconf()
    shelltools.export("CFLAGS", "%s -I/usr/include/db1" % get.CFLAGS())
    libtools.libtoolize("--force")
    autotools.rawConfigure("--host=%s  \
                            --prefix=/usr \
			    --libdir=/usr/lib \
                            --mandir=/usr/share/man \
			    --infodir=/usr/share/info \
			    --sysconfdir=/etc \
			    --localstatedir=/var/lib \
			    --with-kde-datadir=%s/share \
                            --disable-gtk-doc  \
			    --enable-prefer-db1 \
			    --enable-compat185" % (get.HOST(), get.kdeDIR()))
                           
def build():
    #çekil git ordan db4
    shelltools.system("mv /usr/include/db.h /usr/include/db.h_wait")
    shelltools.system("cp db.h /usr/include/db.h")
    autotools.make("-j1")
    shelltools.system("mv /usr/include/db.h_wait /usr/include/db.h")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "ChangeLog", "COPYING*", "INSTALL", "NEWS", "README", "TODO")
