#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Murat Şenel
#
#muratasenel@gmail.com

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = "proj-4.5.0b2"

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.insinto("/usr/lib", "src/*.o")
    pisitools.insinto("/usr/include", "src/*.h")
    pisitools.dodoc("AUTHOR", "ChangeLog", "COPYING", "NEWS", "README")


