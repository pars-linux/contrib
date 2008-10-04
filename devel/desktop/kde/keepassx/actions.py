#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "keepassx-%s" % get.srcVERSION()

def setup():
    shelltools.system("qmake-qt4")

def build():
    autotools.make()

def install():
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())

    # Add translations
    shelltools.system("lrelease-qt4 src/src.pro")
    pisitools.insinto("/usr/share/keepassx/i18n/", "src/translations/*.qm")

    pisitools.dodoc("changelog", "COPYING", "todo")
