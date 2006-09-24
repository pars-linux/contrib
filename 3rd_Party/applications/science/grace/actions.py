#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get 
import os

def setup():
    pisitools.dosed("src/*", "doc/", "/usr/share/doc/%s/html/" % (get.srcTAG()))
    pisitools.dosed("src/xmgrace.c", "examples/", "/usr/share/doc/%s/examples/" % (get.srcTAG()))
    autotools.configure("--enable-grace-home=/usr/share/grace \
                         --with-extra-ldpath \
                         --with-extra-incpath \
                         --with-helpviewer='firefox %s' \
                         --with-fftw \
                         --with-netcdf \
                         --with-debug \
                         --with-jpegdrv \
                         --with-pngdrv")

def build():
    pass

def install():
    pass
