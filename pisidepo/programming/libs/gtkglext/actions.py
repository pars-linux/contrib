#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Murat Şenel
#
#muratasenel@gmail.com

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--disable-glibtest \
                         --disable-gtktest \
                         --with-gdktarget=x11 \
                         --with-x \
                         --with-gl=/usr/lib/opengl/xorg-x11/lib \
                         --with-gl-includedir=/usr/lib/opengl/include")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("README", "AUTHORS", "ChangeLog*", "COPYING*", "TODO")