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

WorkDir = "grass-6.2.0RC1"

def setup():
    shelltools.export("GRASS_XTERM", "konsole")
    autotools.configure("--prefix=%s/opt \
                         --with-x \
                         --without-cxx \
                         --with-jpeg \
                         --with-proj-includes=/usr/include --with-proj-libs=/usr/lib --with-proj-share=/usr/share/proj \
                         --with-tiff \
                         --with-png \
                         --with-mysql=yes --with-mysql-includes=/usr/include/mysql --with-mysql-libs=/usr/lib/mysql \
                         --with-ffmpeg --with-ffmpeg-includes=/usr/include/ffmpeg \
                         --with-opengl \
                         --with-gdal-config=/usr/bin/gdal-config \
                         --with-fftw \
                         --with-freetype --with-freetype-includes=/usr/include/freetype2 \
                         --with-python \
                         --with-nls \
                         --without-opendwg \
                         --with-tcltk \
                         --enable-largefile" % get.installDIR())

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.domove("/opt/grass-6.2.0RC1/locale", "/usr/share")
    pisitools.dodoc("doc/*.txt", "AUTHORS", "CHANGES", "COPYING", "GPL.txt", "README", "SUBMITTING*", "TODO")

    pisitools.domove("/opt/bin/grass62", "/opt/grass-6.2.0RC1/bin")
    pisitools.domove("/opt/bin/gem", "/opt/grass-6.2.0RC1/bin")
    pisitools.removeDir("/opt/bin")

    #change the GISBASE directory to where it should be
    pisitools.dosed("%s/opt/bin/grass62" % get.installDIR(), "GISBASE=/var/tmp/pisi/grass-6.2.0_rc1-2/install/opt/grass-6.2.0RC1","GISBASE=/opt/grass-6.2.0RC1")


    #make a sym link for bin files
    pisitools.dosym("/opt/grass-6.2.0RC1/bin/grass62", "/usr/bin/grass")
    pisitools.dosym("/opt/grass-6.2.0RC1/bin/gem", "/usr/bin/gem")

