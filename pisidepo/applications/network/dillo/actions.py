#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Uğur Çetin <jnmbk@users.sourceforge.net>

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

WorkDir="dillo-0.8.6-i18n-misc-20060709"

def setup():
    autotools.configure("--disable-glibtest \
                         --disable-gtktest \
                         --enable-ipv6 \
                         --disable-dlgui")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("ChangeLog", "AUTHORS", "INSTALL", "NEWS", "README")