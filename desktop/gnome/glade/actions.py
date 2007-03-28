#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "glade3-%s" % get.srcVERSION()

def setup():
    autotools.configure("--enable-python --disable-scrollkeeper")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("AUTHORS","ChangeLog","COPYING*","INSTALL","NEWS","README","TODO")
    # conflict
    pisitools.remove("/usr/share/icons/hicolor/icon-theme.cache")
