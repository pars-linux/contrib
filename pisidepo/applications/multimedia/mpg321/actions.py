#!/usr/bin/python
#-*- coding: UTF-8 -*-
#
# turkay.eren@gmail.com
#######################

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-mpg123-symlink")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS","BUGS","ChangeLog","HACKING","NEWS","README","README.remote","THANKS","TODO")