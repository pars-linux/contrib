#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--disable-plugin-scintilla --disable-plugin-devhelp")

def build():
    autotools.make()

def install():
    autotools.install()
    
    pisitools.dodoc("TODO", "AUTHORS", "ChangeLog", "README", "ROADMAP", "FUTURE")
    pisitools.remove("/usr/share/icons/hicolor/icon-theme.cache")
