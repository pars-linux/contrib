#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Murat Şenel
#
#murattsenell@gmail.com

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="examine"

def setup():
    autotools.aclocal()
    autotools.system("./autogen.sh --prefix=/usr \
                                   --with-gnu-ld \
                                   --with-pic \
                                   --with-ecore=/usr/share/ecore \
                                   --with-ewl=/usr/share/ewl")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "Changelog", "COPYING*", "NEWS", "README", "TODO")