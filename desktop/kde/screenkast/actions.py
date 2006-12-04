#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import kde
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def setup():
    shelltools.export("libxmlpp_CFLAGS","-I/usr/include/libxml++-1.0 -I/usr/lib/libxml++-1.0/include")
    shelltools.export("libxmlpp_LIBS","-L/usr/lib -lxml++-1.0")
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()
    pisitools.dosym("/usr/kde/3.5/bin/isdvncviewer","/usr/bin/isdvncviewer")