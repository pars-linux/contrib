#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
 
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "scythia"

def setup():
    shelltools.system("qmake-qt4 scythia.pro")

def build():
    autotools.make()

def install():
    pisitools.dobin("src/scythia")
    pisitools.insinto("/usr/share/scythia/lang","qm/*")

    pisitools.dohtml("doc/html/*")
    pisitools.doman("doc/man/man3/*.3")
    pisitools.dodoc("AUTHORS", "CHANGELOG", "COPYING")
