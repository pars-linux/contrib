#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "KeePassX-%s" % get.srcVERSION()

def setup():
    shelltools.system("qmake-qt4 prefix=/usr")

def build():
    autotools.make()

def install():
    pisitools.dobin("bin/keepassx")
    pisitools.insinto("/usr/share/", "share/*")

    # Turkish translation
    shelltools.system("lrelease-qt4 src/translations/keepass-tr_TR.ts -qm src/translations/keepass-tr_TR.qm")
    pisitools.insinto("/usr/share/keepassx/i18n/", "src/translations/keepass-tr_TR.qm")
