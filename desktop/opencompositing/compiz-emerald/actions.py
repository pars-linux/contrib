#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "emerald"

def setup():
    shelltools.system("./autogen.sh")
    autotools.configure("--disable-static")

def build():
    autotools.make()

def install():
    autotools.install()

    # Turkish translation
    pisitools.domo("po/tr.po", "tr", "emerald.mo")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS")
