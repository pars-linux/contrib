#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "lapack-lite-%s" % get.srcVERSION()

def setup():
    shelltools.copy("make.inc.example", "make.inc")

    pisitools.dosed("make.inc", "-funroll-all-loops -O3", "%s -funroll-all-loops -O3" % get.CFLAGS())

def build():
    autotools.make()

def install():
    pisitools.dolib_so("SRC/liblapack.so.%s" % get.srcVERSION())
    pisitools.dosym("/usr/lib/liblapack.so.%s" % get.srcVERSION(), "/usr/lib/liblapack.so.3")
    pisitools.dosym("/usr/lib/liblapack.so.%s" % get.srcVERSION(), "/usr/lib/liblapack.so")

    pisitools.dolib_so("BLAS/SRC/libblas.so.%s" % get.srcVERSION())
    pisitools.dosym("/usr/lib/libblas.so.%s" % get.srcVERSION(), "/usr/lib/libblas.so.3")
    pisitools.dosym("/usr/lib/libblas.so.%s" % get.srcVERSION(), "/usr/lib/libblas.so")

    pisitools.dodoc("COPYING", "README")
