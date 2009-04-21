#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

WorkDir = "htmledit"

def setup():
    shelltools.system("lrelease-qt4 src/locale/edit_tr.ts -qm src/locale/edit_tr.qm")
    shelltools.system("qmake-qt4 htmledit.pro")

def build():
    autotools.make()

def install():
    pisitools.dobin("edithtml")

    pisitools.insinto("/usr/share/qt_xhtmledit/locale", "src/locale/*.qm")
    pisitools.insinto("/usr/share/qt_xhtmledit","src/img")
    pisitools.insinto("/usr/share/pixmaps/", "wp.png", "qt_xhtmledit.png")

    pisitools.remove("/usr/share/qt_xhtmledit/img/Thumbs.db")

    pisitools.dodoc("LICENSE")
