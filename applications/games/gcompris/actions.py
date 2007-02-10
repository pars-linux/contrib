#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "gcompris-8.2.2"

def setup():
    autotools.configure("--disable-sdltest \
                         --disable-glibtest \
                         --disable-xf86vidmode \
                         --enable-sqlite \
                         --disable-cairo \
                         --with-python=/usr/bin/python \
                         --with-x")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "ChangeLog", "COPYING", "NEWS", "README*", "THANKS", "TODO")


