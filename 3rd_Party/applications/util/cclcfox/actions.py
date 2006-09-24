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
#   pisitools.dosed("configure", "fox-1.4", "fox-1.6")
#   pisitools.dosed("configure", "FOX-1.4", "FOX-1.6")
#   pisitools.dosed("/src/Makefile.in", "fox-1.4", "fox-1.6")
#   pisitools.dosed("/src/Makefile.am", "fox-1.4", "fox-1.6")    
    autotools.configure()
    #"--x-includes=/usr/include/fox-1.6/fx.h")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "INSTALL", "NEWS", "README", "TODO")
