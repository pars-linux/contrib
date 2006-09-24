#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import kde

WorkDir ="knoda-0.8.2-test1"

def setup():
    kde.configure("--with-hk_classes-dir=/usr/lib/hk_classes \
                   --with-hk_classes-incdir=/usr/include/hk_classes ")

def build():
    kde.make()

def install():
    kde.install()
    pisitools.domo("knoda/po/tr.po", "tr", "knoda.mo")
    pisitools.domove("/usr/share/locale/*", "/usr/kde/3.5/share/locale/")
    pisitools.removeDir("/usr/share")
