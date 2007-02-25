#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools

def setup():
    perlmodules.configure("X11INC=/usr/include/X11/ X11LIB=/usr/lib/X11/ ")

def build():
    perlmodules.make()

def install():
    perlmodules.install()
    pisitools.dodoc("Change.log", "Changes", "COPYING", "INSTALL", "README", "README.linux", "VERSIONS")

