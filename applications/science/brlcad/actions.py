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
    autotools.autoreconf("-fi")
    autotools.configure("--prefix=/usr/brlcad \
                         --disable-almost-everything \
                         --enable-adrt-build \
                         --disable-build-jove \
                         --enable-iwidgets-build=yes \
                         --enable-tnt-build=yes \
                         --with-jdk=/opt/sun-jdk \
                         --disable-static \
                         --without-wgl \
                         --with-python \
                         --with-sdl \
                         --with-pic \
                         --with-x \
                         --enable-optimized \
                         --disable-debug")

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
