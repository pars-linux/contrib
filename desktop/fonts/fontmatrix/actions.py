#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="fontmatrix-0.2svn"

def setup():
    shelltools.system("qmake-qt4 typotek.pro")

def build():
    autotools.make()

def install():
    pisitools.dobin("bin/fontmatrix")

    pisitools.insinto("/usr/share/applications/", "fontmatrix.desktop")
    pisitools.insinto("/usr/share/icons/hicolor/48x48/apps/", "fontmatrix.png")

    pisitools.dodoc("COPYING")
