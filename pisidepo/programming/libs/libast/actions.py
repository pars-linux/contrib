#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Murat Şenel
#
#muratasenel@gmail.com

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="libast-0.7"

def setup():
    autotools.configure("--with-x \
                         --with-imlib \
                         --enable-mmx \
                         --with-regexp \
                         --enable-pcre")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("Changelog", "DESIGN", "README")

