#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Uğur Çetin <jnmbk@users.sourceforge.net>

from pisi.actionsapi import pisitools

def install():
    pisitools.insinto("/usr/share/pilonga", "*.tcl")
    pisitools.dodoc("README", "TODO")
