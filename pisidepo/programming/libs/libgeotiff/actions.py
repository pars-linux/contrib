#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Murat Şenel
#
#murattsenell@gmail.com

from pisi.actionsapi import autotools
from pisi.actionsapi import libtools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

WorkDir = "libgeotiff-1.2.2"

def setup():
    autotools.configure("--with-zip \
                         --with-jpeg \
                         --with-libtiff \
                         --with-proj")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("ChangeLog", "Doxyfile", "HOWTO-RELEASE", "LICENSE", "README*")


