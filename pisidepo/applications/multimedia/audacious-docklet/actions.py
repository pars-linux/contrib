#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Murat Şenel <muratasenel@gmail.com>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="audacious-docklet-0.1.1"

def setup():
    autotools.configure("--enable-nls \
                         --disable-glibtest \
                         --disable-gtktest")
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("ABOUT-NLS", "ChangeLog", "COPYING", "AUTHORS", "INSTALL", "README", "NEWS")

