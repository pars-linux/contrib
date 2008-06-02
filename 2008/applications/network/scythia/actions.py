#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
 
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "scythia"

def setup():
    shelltools.system("qmake-qt4 scythia.pro")

def build():
    autotools.make()

def install():
    pisitools.dobin("bin/scythia")
    pisitools.insinto("/usr/share/scythia/lang","translations/*")

    pisitools.dohtml("doc/html/*")
    pisitools.doman("doc/man/man3/*.3")
    pisitools.dodoc("AUTHORS", "CHANGELOG", "COPYING")
