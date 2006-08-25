#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Murat Şenel
#
#murattsenell@gmail.com

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="examine-0.0.1"

def setup():
    autotools.aclocal()
    autotools.system("./autogen.sh --prefix=/usr \
                                   --with-ecore \
                                   --with-ecore-exec \
                                   --with-ewl \
                                   --with-ewl-exec")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "Changelog", "COPYING*", "NEWS", "README", "TODO")