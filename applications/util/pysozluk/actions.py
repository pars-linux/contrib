#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="PySozluk-%s" % get.srcVERSION()

def install():
    pisitools.dobin("pysozluk")
    pisitools.insinto("/usr/share/pysozluk/bayrak", "bayrak/*")
    pisitools.insinto("/usr/share/pysozluk", "pysozluk_konsole.py")
    pisitools.insinto("/usr/share/pysozluk", "database")
    pisitools.insinto("/usr/share/pysozluk", "config")
    pisitools.insinto("/usr/share/pysozluk/yardim", "yardim/*")
    pisitools.insinto("/usr/share/pysozluk", "pysozluk.py")
    pisitools.insinto("/usr/share/applications", "pysozluk.desktop")
    pisitools.insinto("/usr/share/pixmaps", "pysozluk.png")
    pisitools.dodoc("README", "license.txt")

