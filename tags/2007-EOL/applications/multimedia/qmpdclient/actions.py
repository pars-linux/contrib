#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    shelltools.system("lrelease-qt4 tr_TR.ts -qm tr_TR.qm")
    pisitools.dosed("qmpdclient.pro", "PREFIX = /usr/local", "PREFIX = /usr")
    shelltools.system("qmake-qt4 qmpdclient.pro")

def build():
    autotools.make()

def install():
    pisitools.dobin("qmpdclient")
    pisitools.insinto("/usr/share/QMPDClient/translations/", "tr_TR.qm")

    pisitools.dodoc("AUTHORS", "Changeog", "README", "")
