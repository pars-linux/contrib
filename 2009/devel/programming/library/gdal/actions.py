#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("GDALmake.opt.in", "@datadir@", "@datadir@/gdal")

    autotools.configure("--enable-shared \
                        --disable-static \
                        --with-expat \
                        --without-grass \
                        --without-hdf4 \
                        --without-fme \
                        --without-pcraster \
                        --without-kakadu \
                        --without-mrsid \
                        --without-jp2mrsid \
                        --without-msg \
                        --without-bsb \
                        --without-dods-root \
                        --without-oci \
                        --without-ingres \
                        --without-spatialite \
                        --without-dwgdirect \
                        --without-epsilon \
                        --without-idb \
                        --without-sde \
                        --without-libtool \
                        --with-ogr \
                        --with-grib \
                        --with-vfk \
                        --with-libtiff \
                        --with-geotiff \
                        --with-pg \
                        --with-cfitsio \
                        --with-netcdf \
                        --with-png \
                        --with-jpeg \
                        --with-pcidsk \
                        --with-gif \
                        --with-ogdi \
                        --with-hdf5 \
                        --with-jasper \
                        --with-ecw \
                        --with-xerces \
                        --with-odbc \
                        --with-curl \
                        --with-sqlite3 \
                        --with-mysql \
                        --with-geos \
                        --with-pam \
                        --with-perl \
                        --with-ruby \
                        --with-python \
                        --with-threads \
                        --with-pymoddir=/usr/lib/python2.6/site-packages")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COMMITERS", "HOWTO-RELEASE", "NEWS", "PROVENANCE.TXT", "VERSION")

