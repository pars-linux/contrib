#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "eel-2.17.90"

def setup():
    autotools.configure("--enable-debug")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "ChangeLog", "COPYING*", "HACKING", "MAINTAINERS", "THANKS", "INSTALL", "NEWS", "README", "TODO")