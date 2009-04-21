#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    # rebuild silly configure script
    autotools.autoconf()
    autotools.configure("--enable-release \
                         --disable-libao \
                         --enable-oss \
                         --enable-openssl \
                         --enable-nls \
                         --disable-rpath \
                         --disable-aotest \
                         --disable-glibtest \
                         --disable-gtktest \
                         --disable-esdtest \
                         --with-boost \
                         --with-x")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.insinto("/usr/share/applications", "share/nt.desktop")
    pisitools.insinto("/usr/share/pixmaps", "share/*.png")
    pisitools.insinto("/usr/share/pixmaps", "share/*.xpm")

    pisitools.domo("po/tr.po","tr","d4x.mo")
    pisitools.remove("/usr/share/locale/locale.alias")

    pisitools.doman("DOC/nt.1")
    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "ChangeLog*", "COPYING", "NEWS", "PLANS", "README", "TODO", "DOC/FAQ", "DOC/LICENSE", "DOC/THANKS", "DOC/TROUBLES")
