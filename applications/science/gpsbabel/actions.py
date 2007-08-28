#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--with-zlib=system")

def build():
    autotools.make()

def install():
    pisitools.dobin("gpsbabel")

    pisitools.dohtml("gpsbabel.html")
    pisitools.dodoc("README*", "COPYING", "AUTHORS")
