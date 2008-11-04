#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    shelltools.system("qmake-qt4 PREFIX=/usr")

def build():
    autotools.make()

def install():
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())

    pisitools.remove("/usr/share/texmaker/AUTHORS")
    pisitools.remove("/usr/share/texmaker/CHANGELOG.txt")
    pisitools.remove("/usr/share/texmaker/COPYING")
    pisitools.remove("/usr/share/pixmaps/texmaker.ico")

    pisitools.dodoc("utilities/AUTHORS", "utilities/COPYING", "utilities/CHANGELOG.txt")

    pisitools.domove("/usr/share/texmaker/texmaker.desktop", "/usr/share/applications")
