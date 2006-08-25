#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Uğur Çetin <jnmbk@users.sourceforge.net>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    pass

def build():
    autotools.make()

def install():
    pisitools.insinto("/usr/share/openttd/data", "data/*")
    pisitools.insinto("/usr/share/openttd/lang", "lang/*.lng")
    pisitools.insinto("/usr/share/pixmaps", "media/openttd.128.png")
    pisitools.doexe("openttd", "/usr/share/openttd")
    pisitools.dodoc("docs/*")
    pisitools.dodoc("*.txt")