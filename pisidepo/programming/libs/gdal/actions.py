#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Murat Şenel
#
#muratasenel@gmail.com

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "gdal-1.3.2"

def setup():
    autotools.configure("--with-libz \
                         --with-grass=no \
                         --with-libtool \
                         --without-ld-shared \
                         --enable-static=yes \
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
    autotools.install()
    pisitools.dodoc("COMMITERS", "Doxyfile", "HOWTO-RELEASE", "NEWS", "VERSION")
    pisitools.doman("man/man1/*")
    pisitools.dohtml("html/*")
    pisitools.dohtml("ogr/*")

    #prevent file conflict
    pisitools.removeDir("/usr/lib/perl5")


