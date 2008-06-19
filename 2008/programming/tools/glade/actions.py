#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "glade3-%s" % get.srcVERSION()

def setup():
    autotools.configure("--enable-python \
                         --disable-scrollkeeper")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dosym("/usr/bin/glade-3", "/usr/bin/glade")
    pisitools.remove("/usr/share/icons/hicolor/icon-theme.cache")

    pisitools.dodoc("AUTHORS","ChangeLog","COPYING*","NEWS","README","TODO")
