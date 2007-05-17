#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="Manslide-%s" % get.srcVERSION()

def setup():
    shelltools.system("/usr/bin/qmake-qt4 Manslide.pro")

def build():
    autotools.make()


def install():
    pisitools.dobin("Manslide","/usr/share/manslide")

    pisitools.dosym("/usr/share/manslide/Manslide","/usr/bin/manslide")

    pisitools.insinto("/usr/share/manslide/Effects","Effects/*")
    pisitools.insinto("/usr/share/manslide/Interface","Interface/*")
    pisitools.insinto("/usr/share/manslide/Luma","Luma/*")
    pisitools.insinto("/usr/share/manslide/","*.qm")
