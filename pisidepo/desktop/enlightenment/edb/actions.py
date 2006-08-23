#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Murat Şenel
#
#murattsenell@gmail.com

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="edb-1.0.5.007"

def setup():
    autotools.configure("--prefix=/usr \
                         --disable-libtool-lock \
                         --enable-compat185 \
                         --enable-dump185 \
                         --disable-bigfile \
                         --enable-gtk \
                         --enable-ncurses")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "COPYING*", "README*")