#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Murat Şenel
#
#murattsenell@gmail.com

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "grass-6.1.0"

def setup():
    autotools.configure("--with-x \
                         --enable-shared \
                         --enable-64bit \
                         --enable-64bit-vis \
                         --enable-sysv \
                         --enable-socket \
                         --enable-fifo \
                         --enable-w11 \
                         --with-cxx \
                         --with-jpeg \
                         --with-proj-includes=/usr/include --with-proj-libs=/usr/lib --with-proj-share=/usr/share/proj \
                         --with-tiff \
                         --with-png \
                         --without-mysql \
                         --with-sqlite \
                         --with-ffmpeg=no \
                         --with-postgres=no --with-postgres-includes=/usr/include/postgresql --with-postgres-libs=/usr/lib/postgresql \
                         --with-opengl \
                         --with-gdal-config \
                         --with-gdal \
                         --with-odbc \
                         --with-fftw \
                         --with-motif \
                         --with-freetype --with-freetype-includes=/usr/include/freetype2 \
                         --with-glw \
                         --with-nls \
                         --without-opendwg \
                         --with-curses \
                         --with-tcltk \
                         --enable-largefile \
                         --prefix=%s/opt" % get.installDIR())

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.domove("/opt/grass-6.1.0/locale", "/usr/share/")
    pisitools.dodoc("/doc*.txt", "AUTHORS", "CHANGES", "COPYING", "GPL.txt", "README", "SUBMITTING*", "TODO")

    #change the GISBASE directory to where it should be
    pisitools.dosed("%s/opt/bin/grass61" % get.installDIR(), "GISBASE=/var/tmp/pisi/grass-6.1.0-1/install/opt/grass-6.1.0","GISBASE=/opt/grass-6.1.0")

    #make a sym link for bin files
    pisitools.dosym("/opt/bin/grass61", "/usr/bin/grass61")
    pisitools.dosym("/opt/bin/gem", "/usr/bin/gem")

