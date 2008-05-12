#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def setup():
    shelltools.export("QTDIR", "/usr/qt/4")
    autotools.configure("--prefix=/usr \
                         --with-x \
                         --with-inotify \
                         --disable-static")

    shelltools.cd("qtgui/i18n")
    shelltools.system("lrelease-qt4 *.ts")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("COPYING", "README", "ChangeLog", "VERSION")
