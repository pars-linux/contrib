#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Murat Şenel <muratasenel@gmail.com>

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def setup():
    autotools.aclocal()
    autotools.configure()


def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.domo("po/tr.po","tr","nautilus-sendto.mo")
    pisitools.dodoc("ChangeLog", "AUTHORS", "INSTALL", "COPYING", "NEWS", "README")

