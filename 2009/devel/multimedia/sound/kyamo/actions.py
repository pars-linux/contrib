#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

# paketi alacaklar için notlar:
# kurulum sisteminde sorun var, düzeltilmesi veya elle kurulması gerekebilir
# bu kadar :)
WorkDir = "kyamoqt4-0.50-alpha-3"

def setup():
    shelltools.system("qmake-qt4 PREFIX=/usr")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())
    pisitools.dodoc("Changelog")
