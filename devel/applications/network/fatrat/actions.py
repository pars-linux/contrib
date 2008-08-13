#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def setup():
    cmaketools.configure("-DWITH_NLS=ON \
                          -DWITH_JABBER=ON \
                          -DWITH_SFTP=ON \
                          -DWITH_BITTORRENT=OFF")

def build():
    cmaketools.make()

def install():
    pisitools.dosed("data/fatrat.desktop", "GenericName=FatRat", "GenericName=Download Manager\nGenericName[tr]=Çok İşlevli İndirme Yöneticisi")
    pisitools.dosed("data/defaults.conf", "ispeed_down=131072", "ispeed_down=524288")

    cmaketools.install("DESTDIR=%s"%get.installDIR())

    # Turkish translations
    shelltools.system("lrelease-qt4 locale/fatrat_tr_TR.ts")
    pisitools.insinto("/usr/share/fatrat/lang","locale/fatrat_tr_TR.qm")

    pisitools.dohtml("doc/*")
