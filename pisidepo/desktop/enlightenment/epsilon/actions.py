#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Murat Şenel
#
#murattsenell@gmail.com

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="epsilon-0.3.0.007"

def setup():

    autotools.configure("--prefix=/usr \
                         --enable-ecore \
                         --enable-imlib2 \
                         --enable-epeg \
                         --with-evas-prefix=/usr/share/evas \
                         --enable-edje")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "Changelog", "COPYING", "NEWS", "README", "TODO")