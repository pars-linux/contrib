#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-static \
                         --enable-gpx \
                         --enable-georef \
                         --enable-spit \
                         --with-qtdir=/usr/qt/4 \
                         --with-x \
                         --with-python \
                         --with-grass=/opt/grass-6.2.1 \
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

    pisitools.insinto("/usr/share/pixmaps", "images/icons/qgis-icon.png", "qgis.png")

    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "COPYING", "INSTALL", "NEWS", "README", "TODO")
