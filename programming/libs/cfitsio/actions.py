#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "cfitsio"

def setup():
    autotools.rawConfigure("--prefix=/usr \
                            --libdir=/usr/lib \
                            --includedir=/usr/include")

def build():
    autotools.make("shared")

def install():
    pisitools.dodir("/usr")

    autotools.install()

    pisitools.dosym("/usr/lib/libcfitsio.so.0", "/usr/lib/libcfitsio.so")
    pisitools.remove("/usr/lib/libcfitsio.a")

    pisitools.dodoc("*.ps", "*.txt", "README")
