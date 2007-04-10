#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--enable-static=no \
                         --disable-qt \
                         --disable-gtk \
                         --disable-wxwidgets")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dobin("src/gui/curses/weechat-curses", "/usr/bin")
    pisitools.dosym("/usr/bin/weechat-curses", "/usr/bin/weechat")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "INSTALL", "NEWS", "README")
