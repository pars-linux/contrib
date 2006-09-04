#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Murat Şenel <muratasenel@gmail.com>

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--disable-scrollkeeper \
                         --enable-schemas-install")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.removeDir("/var")
    pisitools.dodoc("ChangeLog", "AUTHORS", "MAINTAINERS", "NEWS", "README", "TODO")

