#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Murat Şenel
#
#muratasenel@gmail.com

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "cfitsio"

def setup():
    autotools.rawConfigure("--prefix=/usr \
                            --libdir=/usr/lib \
                            --includedir=/usr/include")

def build():
    autotools.make()

def install():
    pisitools.dodir("/usr")
    autotools.install()
    pisitools.dodoc("*.ps", "*.txt", "README")

