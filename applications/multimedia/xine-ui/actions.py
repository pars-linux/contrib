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
    autotools.configure("--enable-lirc     \
                         --enable-nls      \
			 --enable-vdr      \
			 --with-x          \
			 --enable-aalib    \
                         --enable-libcaca  \
			 --enable-curl     \
			 --enable-readline \
			 --enable-ncurses  \
			 --enable-debug")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/share/applications", "misc/desktops/xine.desktop")
    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "ChangeLog", "COPYING", "INSTALL", "NEWS", "README")
