#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def setup():
    shelltools.system("qmake-qt4")

def build():
    autotools.make()

def install():
    pisitools.dobin("bin/*")
    pisitools.insinto("/usr/share/pixmaps","pokerth.png")

    pisitools.dodoc("ChangeLog","COPYING")
