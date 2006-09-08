#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Uğur Çetin <jnmbk@users.sourceforge.net>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir="fltk-2.0.x-r4886"

def setup():
    autotools.autoconf()
    autotools.configure("--enable-shared")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("documentation/*")