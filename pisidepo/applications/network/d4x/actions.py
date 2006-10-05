#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Murat Şenel
#
#muratasenel@gmail.com

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir="d4x-2.5.7.1"

def setup():
    autotools.configure("--enable-release \
                         --enable-esd \
                         --enable-alsa \
                         --enable-libao \
                         --enable-openssl \
                         --enable-nls \
                         --disable-rpath \
                         --disable-aotest \
                         --disable-esdtest \
                         --disable-glibtest \
                         --disable-gtktest \
                         --with-gnu-ld \
                         --with-included-gettext \
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

