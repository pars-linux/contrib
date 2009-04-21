#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "CdCat-%s/src" % get.srcVERSION()

def setup():
    shelltools.system("qmake")

def build():
    autotools.make()

def install():
    autotools.install("INSTALL_ROOT=%s" % get.installDIR())
    shelltools.cd("..")

    pisitools.insinto("/usr/share/applications","KDE/cdcat.desktop")
    pisitools.insinto("/usr/share/pixmaps","cdcat.png")

    pisitools.dodoc("Authors", "ChangeLog", "COPYING", "README", "README_IMPORT", "TODO")
