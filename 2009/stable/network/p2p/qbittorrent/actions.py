#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.rawConfigure("--prefix=/usr \
                            --bindir=/usr/bin \
                            --datadir=/usr/share \
                            --qtdir=/usr/qt/4")

def build():
    autotools.make("CXX=%s" % get.CXX())

def install():
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())

    pisitools.dosym("/usr/share/icons/hicolor/128x128/apps/qbittorrent.png", "/usr/share/pixmaps/qbittorrent.png")

    pisitools.dodoc("AUTHORS", "Changelog", "COPYING", "NEWS", "README", "TODO")
