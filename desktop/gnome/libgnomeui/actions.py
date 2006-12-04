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

def setup():
    shelltools.copy("aclocal.m4", "old_macros.m4")
    shelltools.export("AT_M4DIR", "")
    shelltools.export("WANT_AUTOCONF", "1.7")
    autotools.autoconf()
    autotools.configure("--enable-jpeg")

def build():
    autotools.make("-j1")

def install():
    autotools.install()
#   autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "ChangeLog", "COPYING*", "INSTALL", "NEWS", "README", "TODO")