#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Eren Türkay <turkay.eren@gmail.com>

from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="qjoypad-3.4/src"

def setup():
    shelltools.system("mkdir -p %s/usr" % get.installDIR())
    shelltools.system("./config --prefix=%s/usr" % get.installDIR())

def build():
    shelltools.system("make")

def install():
    shelltools.system("make install")
    shelltools.system("mv %s/usr/doc %s/usr/share" % (get.installDIR(),get.installDIR()))