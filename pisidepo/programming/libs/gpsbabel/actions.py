#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir="gpsbabel-1.3.1"

def setup():
    autotools.configure("--enable-shapefile=yes \
                         --enable-pdb=yes \
                         --enable-csv=yes \
                         --enable-filters=yes \
                         --with-cet=all \
                         --with-zlib=system \
                         --with-expathdr=/usr/include \
                         --with-libexpat=/usr/lib")

def build():
    autotools.make()

def install():
    pisitools.dobin("gpsbabel")
    pisitools.dodoc("AUTHORS", "COPYING", "INSTALL", "NEWS", "README*")
    pisitools.dohtml("*")
