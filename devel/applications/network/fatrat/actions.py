#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    cmaketools.configure("-DWITH_NLS=ON \
                          -DWITH_JABBER=ON \
                          -DWITH_SFTP=ON \
                          -DWITH_WEBINTERFACE=ON \
                          -DWITH_BITTORRENT=ON")

def build():
    cmaketools.make()

def install():
    pisitools.dosed("data/fatrat.desktop", "GenericName=FatRat", "GenericName=Download Manager\nGenericName[tr]=Çok İşlevli İndirme Yöneticisi")
    pisitools.dosed("data/defaults.conf", "ispeed_down=131072", "ispeed_down=524288")

    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dohtml("doc/*")
