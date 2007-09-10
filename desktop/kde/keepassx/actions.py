#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.system("/usr/bin/qmake-qt4 prefix=/usr")

def build():
    autotools.make()

def install():
    pisitools.dobin("bin/keepass")
    pisitools.insinto("/usr/share/", "share/*")

    # Turkish translation
    shelltools.system("lrelease-qt4 src/translations/keepass-tr_TR.ts -qm src/translations/keepass-tr_TR.qm")
    pisitools.insinto("/usr/share/keepass/i18n/", "src/translations/keepass-tr_TR.qm")