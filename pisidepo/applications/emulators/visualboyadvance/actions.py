#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Uğur Çetin <jnmbk@users.sourceforge.net>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir="VisualBoyAdvance-1.7.2"

def setup():
    autotools.configure("--disable-sdltest")
    #TODO: --enable-gtk

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("README", "NEWS", "AUTHORS", "COPYING")
