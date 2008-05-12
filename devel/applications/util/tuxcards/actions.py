#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("tuxcards.pro", "/usr/local/doc/tuxcards", "/usr/share/tuxcards")
    pisitools.dosed("tuxcards.pro", "/usr/local", "/usr")
    pisitools.dosed("src/CTuxCardsConfiguration.cpp", "/usr/local/doc/tuxcards", "/usr/share/tuxcards")
    pisitools.dosed("src/gui/dialogs/optionsDialog/IOptionsDialog.ui", "/usr/local/bin", "/usr/bin")
    shelltools.system("/usr/qt/3/bin/qmake tuxcards.pro")

def build():
    autotools.make()

def install():
    pisitools.dodoc("COPYING", "AUTHORS")
    pisitools.dohtml("docs/en/*")
    pisitools.insinto("/usr/share/pixmaps", "src/icons/lo32-app-tuxcards.xpm", "tuxcards.xpm")
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())
