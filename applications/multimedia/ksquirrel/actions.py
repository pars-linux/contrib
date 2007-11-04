#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import kde
from pisi.actionsapi import pisitools

def setup():
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()

    pisitools.domo("po/tr.po","tr","ksquirrel.mo")
    pisitools.domove("/usr/share/locale/tr", "%s/share/locale" % get.kdeDIR())
    pisitools.removeDir("/usr/share")
