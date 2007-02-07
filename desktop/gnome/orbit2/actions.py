#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = 'ORBit2-2.14.5'

def setup():
    autotools.configure("--enable-static=no")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "ChangeLog", "COPYING*", "INSTALL", "NEWS", "README", "TODO")
    # remove gtk-doc directory, it is created although --enable-gtk-doc is default no... damn!
    pisitools.removeDir("/usr/share/gtk-doc")
