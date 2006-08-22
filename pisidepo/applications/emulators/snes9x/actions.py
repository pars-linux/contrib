#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Uğur Çetin <jnmbk@users.sourceforge.net>

from pisi.actionsapi import pisitools

def setup():
    pass

def build():
    pass

def install():
    pisitools.dobin("snes9x")
    pisitools.dodoc("*.txt", "readme.unix", "config.info")