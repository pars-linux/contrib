#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.system("/usr/qt/3/bin/qmake")

def build():
    autotools.make("-j2")

def install():
    pisitools.insinto("/usr/share/qtsozluk", "veriler/*.e2t")
    pisitools.insinto("/usr/share/qtsozluk", "veriler/*.t2e")
    pisitools.insinto("/usr/share/applications", "veriler/qtsozluk.desktop")
    pisitools.insinto("/usr/share/pixmaps", "veriler/qtsozluk.png")

    pisitools.dobin("cevir/entr/turkceyecevir")
    pisitools.dobin("cevir/tren/ingilizceyecevir")
    pisitools.dobin("qtsozluk/qtsozluk")
    pisitools.dobin("sozluk/sozluk")

    pisitools.dodoc("COPYING", "README")
