#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def build():
    autotools.make()

def install():
    # Makefile has installation path problems so we make our own installation
    pisitools.dobin("wordplay")
    pisitools.insinto("/usr/share/wordplay","data/*")
    pisitools.insinto("/usr/share/wordplay","tilesets")
    pisitools.insinto("/usr/share/wordplay","wordplay_*.png")
    pisitools.dodoc("AUTHORS", "COPYING", "README", "NEWS", "INSTALL", "ChangeLog")
