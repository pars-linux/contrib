#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    autotools.autoconf()
    autotools.rawConfigure("--with-pgsql \
                            --with-geos \
                            --with-geos-libdir=/usr/lib \
                            --with-proj \
                            --with-proj-libdir=/usr/lib \
                            --with-docdir=/usr/share/doc/%s \
                            --datadir=/usr/share/postgresql/contrib \
                            --libdir=/usr/lib/postgresql" % get.srcTAG())

def build():
    autotools.make()
    shelltools.cd("topology")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.cd("topology")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.cd("..")

    pisitools.dodoc("CHANGES", "COPYING", "CREDITS", "TODO", "README.*", "doc/README")
    pisitools.dohtml("doc/html/*")
    pisitools.doman("doc/man/*")
