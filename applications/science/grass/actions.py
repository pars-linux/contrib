#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "grass-6.3.0RC1"

def setup():
    autotools.configure("--disable-static \
                         --enable-shared \
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
                         --enable-largefile")

def build():
    autotools.make()

def install():
    # Change the GISBASE directory to where it should be
    pisitools.dosed("bin.i686-pc-linux-gnu/grass63", "GISBASE=\"%s/%s/dist.i686-pc-linux-gnu\"" % (get.workDIR(), WorkDir), "GISBASE=/opt/grass")

    autotools.rawInstall("INST_DIR=%s/opt/grass" % get.installDIR())

    pisitools.dobin("bin.i686-pc-linux-gnu/grass63")

    pisitools.dodoc("doc/*.txt", "AUTHORS", "CHANGES", "COPYING", "GPL.txt", "README", "SUBMITTING*", "TODO")
