#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Murat Şenel <muratasenel@gmail.com>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="stellarium-0.8.1"

def setup():
    autotools.configure("--enable-nls \
                         --disable-sdltest \
                         --with-x")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("ABOUT-NLS", "ChangeLog", "AUTHORS", "INSTALL", "COPYING", "NEWS", "README", "TODO")

