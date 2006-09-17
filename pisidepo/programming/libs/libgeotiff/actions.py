#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Murat Şenel
#
#muratasenel@gmail.com

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "libgeotiff-1.2.3"

def setup():
    autotools.configure("--with-zip \
                         --with-jpeg \
                         --with-libtiff \
                         --with-proj")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("ChangeLog", "Doxyfile", "HOWTO-RELEASE", "LICENSE", "README*", "docs/manual.txt")
    pisitools.dohtml("docs/*")
    pisitools.remove("/usr/share/doc/%s/README.WIN" % get.srcTAG())


