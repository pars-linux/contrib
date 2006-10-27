#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


def setup():
    shelltools.export("R_HOME_DIR", "/usr/lib/R")
    autotools.configure("--enable-R-profiling --enable-R-shlib --enable-shared --with-tcltk --with-tcl-config=/usr/lib/tclConfig.sh --with-tk-config=/usr/lib/tkConfig.sh --with-system-pcre --with-system-zlib --with-system-bzlib --with-jpeglib --with-png --with-readline --with-blas --enable-mbcs --enable-utf8")

def build():
    autotools.make()



def install():
    autotools.install()
    pisitools.removeDir("/usr/bin")
    pisitools.remove("/usr/lib/R/bin/R")
    pisitools.dosym("/usr/lib/R/bin/R","/usr/bin/R")