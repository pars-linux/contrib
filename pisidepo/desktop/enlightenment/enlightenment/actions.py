#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Murat Şenel
#
#murattsenell@gmail.com

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="enlightenment-0.16.999.032"

def setup():
    autotools.configure("--enable-nls \
                         --disable-rpath \
                         --enable-x \
                         --with-gnu-ld \
                         --enable-libiconv \
                         --enable-libintl \
                         --enable-esd-sound \
                         --enable-xinerama \
                         --enable-xrandr \
                         --enable-upgrade \
                         --enable-hints-ewmh \
                         --enable-fsstd \
                         --enable-zoom \
                         --with-imlib2 \
                         --enable-evas-config \
                         --enable-ecore-config \
                         --enable-edje_cc \
                         --enable-edje \
                         --enable-eet-config \
                         --enable-embryo-config \
                         --enable-profile")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.domo("po/tr.po","tr","enlightenment.mo")
    pisitools.dodoc("AUTHORS", "ChangeLog", "INSTALL", "NEWS", "README*", "docs/README*")

