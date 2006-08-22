#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Murat Şenel
#
#murattsenell@gmail.com

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "gcompris-8.0BETA4"

def setup():
    autotools.autoconf()
    autotools.configure("--enable-binreloc \
                         --disable-sdltest \
                         --disable-glibtest \
                         --disable-xf86vidmode \
                         --enable-sqlite \
                         --with-python=/usr/bin/python \
                         --with-x")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "ChangeLog", "COPYING", "NEWS", "README*", "THANKS", "TODO")


