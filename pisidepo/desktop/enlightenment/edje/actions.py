#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Murat Şenel
#
#murattsenell@gmail.com

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir="edje-0.5.0.027"

def setup():
    autotools.configure("--prefix=/usr \
                         --with-pic \
                         --with-eet \
                         --with-evas \
                         --with-ecore=/usr/lib \
                         --with-embryo")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "Changelog", "COPYING*", "NEWS", "README")