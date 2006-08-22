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
    pisitools.dodir("/usr/share/openttd")
    pisitools.dodir("/usr/share/openttd/data")
    pisitools.dodir("/usr/share/openttd/lang")
    pisitools.dodir("/usr/share/pixmaps/")
    pisitools.doexe("openttd", "/usr/share/openttd")
    pisitools.dodoc("docs/*")
    pisitools.dodoc("*.txt")
    pisitools.dobin("data/*", "/usr/share/openttd/data")
    pisitools.dobin("lang/*.lng", "/usr/share/openttd/lang")
    pisitools.dobin("media/openttd.128.png", "/usr/share/pixmaps")