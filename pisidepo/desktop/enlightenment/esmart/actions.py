#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Murat Şenel
#
#murattsenell@gmail.com

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="esmart-0.9.0.007"

def setup():
    autotools.configure("--prefix=/usr \
                         --enable-evas \
                         --with-ecore \
                         --with-imlib2=/usr/share/imlib2 \
                         --with-epsilon \
                         --with-edje=/usr/share/edje")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "Changelog", "COPYING*", "NEWS", "README")

