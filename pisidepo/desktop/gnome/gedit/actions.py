#!/usr/bin/python
#-*- coding: UTF-8 -*-
#
# Uğur Çetin
# jnmbk@users.sourceforge.net

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--disable-scrollkeeper")
    #TODO:--enable-python

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "MAINTAINERS", "NEWS", "README", "THANKS", "TODO")
    pisitools.removeDir("/var")