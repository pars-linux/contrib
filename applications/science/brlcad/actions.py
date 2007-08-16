#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools

def setup():
    shelltools.system("sh autogen.sh")
    shelltools.export("LIBS","-lz -lrle")

    autotools.configure("--enable-jove-build=no \
                         --enable-termlib-build=no \
                         --enable-regexp-build=no \
                         --enable-png-build=no \
                         --enable-zlib-build=no \
                         --enable-tcl-build=no \
                         --enable-tk-build=no \
                         --enable-itcl-build=no \
                         --enable-itk-build=no \
                         --enable-iwidgets-build=yes \
                         --enable-urt-build=no \
                         --with-java=/opt/sun-jdk \
                         --disable-static \
                         --without-wgl \
                         --with-python \
                         --with-sdl \
                         --with-pic \
                         --enable-optimized \
                         --disable-debug \
                         --prefix=/usr/brlcad/")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # for docs
    pisitools.removeDir("/usr/share/doc")
    pisitools.removeDir("/usr/share/html")

    for docs in ["doc/*.txt","doc/*.tr","doc/legal","doc/IDEAS","doc/PROJECTS","AUTHORS","COPYING","README","NEWS"]:
        pisitools.insinto("/usr/share/doc/%s" % get.srcTAG(), docs)

    pisitools.dohtml("doc/html/")
