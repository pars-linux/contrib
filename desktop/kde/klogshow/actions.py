#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools

def setup():
    cmaketools.configure()

def build():
    cmaketools.make()

def install():
    cmaketools.install()

    pisitools.dobin("src/klogshow")
    pisitools.insinto("/usr/share/applications","src/klogshow.desktop")
    pisitools.insinto("/usr/share/pixmaps","src/images/klogshow.png")

    pisitools.dodoc("CHANGELOG", "COPYING")
