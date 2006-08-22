#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Murat Şenel
#
#murattsenell@gmail.com

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="ewl-0.0.4.007"

def setup():
    autotools.configure("--prefix=/usr \
                         --with-evas=/usr/share/evas \
                         --with-ecore=/usr/share/ecore \
                         --with-emotion=/usr/share/emotion \
                         --with-edje=/usr/share/edje \
                         --with-edge-png \
                         --enable-software-x11 \
                         --enable-opengl \
                         --enable-fbcon")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "Changelog", "COPYING*", "NEWS", "README", "TODO")