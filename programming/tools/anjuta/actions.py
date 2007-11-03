#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.aclocal()
    autotools.autoconf("-f")
    autotools.configure("--disable-plugin-scintilla \
                         --disable-plugin-devhelp \
                         --disable-scrollkeeper")

def build():
    autotools.make()

def install():
    autotools.install()

    # conflict
    pisitools.remove("/usr/share/icons/hicolor/icon-theme.cache")

    pisitools.dodoc("TODO", "AUTHORS", "ChangeLog", "README", "ROADMAP", "FUTURE")
