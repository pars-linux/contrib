#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = "libgeda-20061020"

def setup():
    autotools.configure("--disable-static \
                         --disable-shared \
                         --disable-gdgeda \
                         --disable-dependency-tracking")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("AUTHORS","BUGS","ChangeLog","README")
