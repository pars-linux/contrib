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
    autotools.configure("--disable-static \
                         --enable-gtk \
                         --enable-cli \
                         --enable-libnotify \
                         --enable-daemon")

    # For daemon config files.
    pisitools.dodir("%s/etc/transmission-daemon")

def build():
    autotools.make()

    shelltools.cd("qt/")
    shelltools.system("qmake-qt4 qtr.pro")
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("COPYING", "AUTHORS", "README", "ChangeLog", "NEWS")

    shelltools.cd("qt/")
    autotools.rawInstall("INSTALL_ROOT=%s/usr" % get.installDIR())
    pisitools.dosym("/usr/bin/qtr", "/usr/bin/transmission-qt")

    pisitools.insinto("%s/%s" % (get.docDIR(), get.srcNAME()),
                       "README.txt", "README-QT")

    pisitools.remove("/usr/share/icons/hicolor/icon-theme.cache")
