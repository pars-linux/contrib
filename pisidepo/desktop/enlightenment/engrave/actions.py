#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Murat Şenel
#
#murattsenell@gmail.com

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="engrave-0.1.0"

def setup():
    autotools.system("./autogen.sh --prefix=/usr \
                                   --enable-dmalloc \
                                   --with-ecore \
                                   --with-ecore-exec \
                                   --with-evas \
                                   --with-evas-exec")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "Changelog", "COPYING*", "NEWS", "README", "TODO")