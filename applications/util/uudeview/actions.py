#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.autoreconf("-f")
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    for libs in ["uulib/libuu.la", "uulib/.libs/libuu.so"]:
        pisitools.doexe(libs, "/usr/lib")

    pisitools.dosym("/usr/lib/libuu.so", "/usr/lib/libuu.so.0")
    pisitools.dosym("/usr/lib/libuu.so", "/usr/lib/libuu.so.0.0.0")

    for includes in ["uulib/fptools.h", "uulib/uudeview.h", "uulib/uuint.h"]:
        pisitools.insinto("/usr/include", includes)

    pisitools.remove("/usr/lib/libuu.la")

    pisitools.dodoc("COPYING", "README","HISTORY", "doc/*")
