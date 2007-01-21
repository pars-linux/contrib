#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools

def setup():
    kde.configure("--with-external-geoip")

def build():
    kde.make()

def install():
    kde.install()
    pisitools.domo("po/tr.po","tr","tork.mo")
    pisitools.domove("/usr/share/locale/tr/LC_MESSAGES/tork.mo","/usr/kde/3.5/share/locale/tr/LC_MESSAGES")
    pisitools.removeDir("/usr/kde/3.5/share/icons/crystalsvg")
