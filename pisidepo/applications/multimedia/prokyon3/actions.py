#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="prokyon3-0.9.6RC1"

def setup():
    autotools.configure("--with-x \
                         --with-qtdir=%s \
                         --with-qt-includes=%s/include \
                         --with-qt-libs=%s \
                         --with-taglib \
                         --with-musicextras \
                         --with-mixxx \
                         --with-musicbrainz \
                         --with-ogg \
                         --with-mad \
                         --with-id3 \
                         --with-mysql --with-mysql-lib --with-mysql-include" % (get.qtDIR(), get.qtDIR(), get.qtLIBDIR()))

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/applications", "prokyon3.desktop")
    pisitools.insinto("/usr/share/pixmaps", "images/prokyon_logo.png", "prokyon.png")

    pisitools.domove("usr/share/prokyon3/html", "%s/%s" % (get.docDIR(), get.srcTAG()))
    pisitools.dodoc("ChangeLog", "AUTHORS", "COPYING", "INSTALL", "NEWS", "README")

