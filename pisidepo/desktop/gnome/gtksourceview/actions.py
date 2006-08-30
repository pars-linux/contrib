#!/usr/bin/python
#-*- coding: UTF-8 -*-
#
# Uğur Çetin
# jnmbk@users.sourceforge.net

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--disable-build-tests")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("AUTHORS", "ChangeLog", "HACKING", "MAINTAINERS", "NEWS", "README", "TODO")