#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.copy("aclocal.m4", "old_macros.m4")
    autotools.aclocal("-I .")
    autotools.autoconf()
    autotools.automake()
    libtools.libtoolize("--copy --force")
    autotools.configure("--enable-ipv6 --enable-esd")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS","ChangeLog","HACKING","NEWS","README")
