#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "xsane-0.991"

def setup():
    autotools.configure("--enable-gtk2 --enable-nls --enable-jpeg --enable-png --enable-tiff --enable-gimp")

def build():
    autotools.make()


def install():
    autotools.install()
    pisitools.dodoc("xsane.[A-Z]*")
    pisitools.dohtml("doc/*")
    pisitools.dosym("/usr/bin/xsane", "/usr/lib/gimp/2.0/plug-ins/xsane")