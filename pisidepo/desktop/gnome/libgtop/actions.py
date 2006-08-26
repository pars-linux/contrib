#!/usr/bin/python
#-*- coding: UTF-8 -*-
#
# turkay.eren@gmail.com

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-static \
                         --enable-gdbm")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS","ChangeLog","NEWS","README","copyright.txt")