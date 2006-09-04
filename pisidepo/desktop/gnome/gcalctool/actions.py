#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Murat Şenel <muratasenel@gmail.com>

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

WorkDir="gcalctool-5.8.24"

def setup():
    autotools.configure("--disable-scrollkeeper \
                         --disable-schemas-install")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.removeDir("/var")
    pisitools.dodoc("ChangeLog*", "AUTHORS", "MAINTAINERS", "NEWS", "README", "TODO")

