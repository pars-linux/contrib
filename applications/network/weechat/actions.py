#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--enable-static=no \
                         --bindir=/usr/bin \
                         --disable-qt \
                         --disable-gtk \
                         --datadir=/usr/share ")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dobin("src/gui/curses", "/usr/bin/weechat-curses")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "INSTALL", "NEWS", "README")
