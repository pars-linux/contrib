#!/usr/bin/python
#-*- coding: utf-8 -*-
#
# murattsenell@gmail.com
#######################

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "enigma-0.92"

def setup():
    autotools.configure("--prefix=/usr --disable-dependency-tracking --enable-optimize")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "README", "Changelog", "NEWS")
