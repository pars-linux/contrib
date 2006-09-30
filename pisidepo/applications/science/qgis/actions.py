#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Murat Şenel <muratasenel@gmail.com>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="qgis-0.7.4"

def setup():
    autotools.configure("--enable-gpx \
                         --enable-georef \
                         --enable-spit \
                         --with-qtdir=/usr/qt/3 \
                         --with-x \
                         --with-grass=/opt/grass-6.2.0RC1 \
                         --with-geos=/usr/bin/geos-config \
                         --with-gdal=/usr/bin/gdal-config \
                         --with-projdir=/usr \
                         --with-sqlite3 \
                         --with-postgresql \
                         --with-gsl")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "COPYING", "INSTALL", "NEWS", "README", "TODO")
