#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "ORBit-0.5.17"

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "ChangeLog", "COPYING*", "INSTALL", "NEWS", "README", "TODO")