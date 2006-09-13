#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Murat Şenel <muratasenel@gmail.com>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="prokyon3-0.9.5RC1"

def setup():
    autotools.configure("--with-x \
                         --with-qtdir=/usr/qt/3 \
                         --with-qt-includes=/usr/qt/3/include \
                         --with-qt-libs=/usr/qt/3/lib \
                         --with-taglib \
                         --with-musicextras \
                         --with-mixxx \
                         --with-musicbrainz \
                         --with-ogg \
                         --with-mad \
                         --with-id3 \
                         --with-mysql --with-mysql-lib --with-mysql-include")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/share/applications", "prokyon3.desktop")
    pisitools.insinto("/usr/share/pixmaps", "images/prokyon_logo.png")
    pisitools.dodoc("ChangeLog", "AUTHORS", "COPYING", "INSTALL", "NEWS", "README")

