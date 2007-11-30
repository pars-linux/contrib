#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.system("qmake-qt4")

def build():
    autotools.make()

def install():
    pisitools.dobin("bin/kotaci")
    pisitools.insinto("/usr/share/applications", "data/kotaci.desktop")

    pisitools.dodoc("AUTHORS", "COPYING", "README", "TODO")
