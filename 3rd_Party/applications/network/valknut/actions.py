#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-ssl --with-libdc=/usr --with-qt-dir=%s" % get.qtDIR())

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/share/pixmaps/", "valknut/icons/icon_32x32.png", "valknut.png")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "COPYING.OpenSSL", "INSTALL", "INSTALL.MAC", "NEWS", "README", "TODO")