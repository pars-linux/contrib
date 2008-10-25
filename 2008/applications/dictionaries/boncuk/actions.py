#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.system("qmake-qt4 boncuk.pro")

    # Change C/XXFLAGS
    pisitools.dosed("Makefile", "CFLAGS        = -pipe -O2", "CFLAGS        = %s" % get.CFLAGS())
    pisitools.dosed("Makefile", "CXXFLAGS      = -pipe -O2", "CXXFLAGS      = %s" % get.CXXFLAGS())

def build():
    shelltools.system("lupdate-qt4 boncuk.pro")
    shelltools.system("lrelease-qt4 boncuk.pro")
    autotools.make()

def install():
    pisitools.dobin("bin/boncuk")
    pisitools.insinto("/usr/share/pixmaps", "resources/boncuk.png")

    pisitools.dodoc("AUTHORS", "COPYING", "README", "TODO")
