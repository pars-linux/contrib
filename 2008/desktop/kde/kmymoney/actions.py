#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools

WorkDir = "kmymoney2-0.9"

def setup():
    kde.configure()

def build():
    kde.make()

def install():
    pisitools.domo("po/tr.po","tr","kmymoney2.mo")
    pisitools.domove("/usr/share/locale/*", "/usr/kde/3.5/share/locale/")
    kde.install()