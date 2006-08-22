#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Erhan Onur Şendağ <onursendag@yahoo.com>


from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    autotools.configure(¨--disable-dbus --enable-hal --enable-debug¨)
#  --enable-hal --enable-dbus --enable-sn --enable-gui   --enable-gconf --enable-amazon    

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "ChangeLog", "COPYING", "INSTALL", "NEWS", "README", "TODO")
