#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "Manslide-%s" % get.srcVERSION()

def setup():
    shelltools.system("qmake-qt4 Manslide.pro")

def build():
    autotools.make()

def install():
    for data in ["Manslide","BIB_ManSlide","Interface", "*.qm"]:
        pisitools.insinto("/usr/share/manslide",data)

    pisitools.dosym("/usr/share/manslide/Manslide","/usr/bin/manslide")
