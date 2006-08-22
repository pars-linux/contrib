#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Murat Şenel
#
#murattsenell@gmail.com

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="emotion"

def setup():

    autotools.system("./autogen.sh --prefix=/usr \
                                   --enable-eet \
                                   --with-evas-prefix=/usr/share/evas \
                                   --enable-edje \
                                   --with-ecore-prefix=/usr/share/ecore \
                                   --with-embryo-prefix=/usr/share/embryo \
                                   --enable-xine")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "Changelog", "COPYING*", "NEWS", "README", "TODO")