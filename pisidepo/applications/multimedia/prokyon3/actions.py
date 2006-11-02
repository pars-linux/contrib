#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="prokyon3-0.9.5"

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

