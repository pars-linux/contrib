#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("GRASS_XTERM", "/usr/bin/konsole")
    autotools.configure("--prefix=%s/opt \
                         --with-x \
                         --with-cxx \
                         --with-jpeg \
                         --with-proj-includes=/usr/include --with-proj-libs=/usr/lib --with-proj-share=/usr/share/proj \
                         --with-tiff \
                         --with-png \
                         --with-mysql=yes --with-mysql-includes=/usr/include/mysql --with-mysql-libs=/usr/lib/mysql \
                         --with-ffmpeg --with-ffmpeg-includes=/usr/include/ffmpeg \
                         --with-opengl \
                         --with-gdal-config=/usr/bin/gdal-config \
                         --with-postgres=yes --with-postgres-includes=/usr/include/postgresql \
                         --with-postgres-libs=/usr/lib/postgresql \
                         --with-fftw \
                         --with-freetype --with-freetype-includes=/usr/include/freetype2 \
                         --with-python \
                         --with-nls \
                         --with-tcltk \
                         --with-readline \
                         --enable-largefile" % get.installDIR())

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.domove("/opt/grass-%s/locale" % get.srcVERSION(), "/usr/share")
    pisitools.dodoc("doc/*.txt", "AUTHORS", "CHANGES", "COPYING", "GPL.txt", "README", "SUBMITTING*", "TODO")

    pisitools.domove("/opt/bin/grass62", "/opt/grass-%s/bin" % get.srcVERSION())
    pisitools.domove("/opt/bin/gem", "/opt/grass-%s/bin" % get.srcVERSION())
    pisitools.removeDir("/opt/bin")

    #change the GISBASE directory to where it should be
    pisitools.dosed("%s/opt/grass-%s/bin/grass62" % (get.installDIR(), get.srcVERSION()), "GISBASE=%s/opt/grass-%s" % (get.installDIR(), get.srcVERSION()), "GISBASE=/opt/grass-%s" % get.srcVERSION())


    #make a sym link for bin files
    pisitools.dosym("/opt/grass-%s/bin/grass62" % get.srcVERSION(), "/usr/bin/grass")
    pisitools.dosym("/opt/grass-%s/bin/gem" % get.srcVERSION(), "/usr/bin/gem")

