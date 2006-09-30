#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Murat Şenel <muratasenel@gmail.com>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="postgis-1.1.4"

def setup():
    autotools.autoconf()
    autotools.rawConfigure("--with-pgsql \
                            --with-geos \
                            --with-geos-libdir=/usr/lib \
                            --with-proj=/usr \
                            --with-proj-libdir=/usr/lib \
                            --datadir=/usr/share/postgresql/contrib \
                            --libdir=/usr/lib/postgresql")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("CHANGES", "COPYING", "CREDITS", "TODO", "README.*", "doc/README")
    pisitools.dohtml("doc/html/*")
    pisitools.doman("doc/man/*")
