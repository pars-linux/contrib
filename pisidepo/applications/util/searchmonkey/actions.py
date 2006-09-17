#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Uğur Çetin <jnmbk@users.sourceforge.net>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.domo("po/tr.po", "tr", "searchmonkey.mo")
    pisitools.domove("/usr/share/searchmonkey/pixmaps", "/usr/share")