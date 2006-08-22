#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Murat Şenel
#
#murattsenell@gmail.com

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="etk"

def setup():
    autotools.system("./autogen.sh --prefix=/usr \
                                   --enable-nls \
                                   --with-gnu-ld \
                                   --with-libiconv")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.domo("po/tr.po","tr","etk.mo")
    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "Changelog", "COPYING*", "NEWS", "README*")