#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "gdal-1.4.0beta2"

def setup():
    pisitools.dosed("GDALmake.opt.in", "@datadir@", "@datadir@/gdal")
    autotools.configure("--with-libz \
                         --with-grass=no \
                         --with-libtool \
                         --without-ld-shared \
                         --enable-static=no \
                         --enable-shared=yes \
                         --with-pic \
                         --with-libgrass=no \
                         --with-cfitsio=yes \
                         --with-pcraster=internal \
                         --with-netcdf \
                         --with-png \
                         --with-libtiff \
                         --with-geotiff=/usr/lib \
                         --with-jpeg \
                         --with-gif \
                         --with-ogdi \
                         --without-hdf5 \
                         --with-jasper \
                         --with-mrsid=no \
                         --with-jp2mrsid=yes \
                         --without-bsb \
                         --with-mysql \
                         --with-xerces \
                         --with-odbc \
                         --with-sqlite \
                         --with-pg \
                         --with-ogr \
                         --with-static-proj4 \
                         --with-geos \
                         --with-php \
                         --with-perl \
                         --with-ruby \
                         --with-python")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COMMITERS", "Doxyfile", "HOWTO-RELEASE", "NEWS", "VERSION")


