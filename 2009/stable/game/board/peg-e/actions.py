#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("qmake-qt4 PREFIX=/usr")

def build():
    autotools.make()

def install():
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())
    pisitools.dodoc("ChangeLog", "COPYING", "README")
    pisitools.dosym("/usr/share/icons/hicolor/48x48/apps/peg-e.png", "/usr/share/pixmaps/peg-e.png")
