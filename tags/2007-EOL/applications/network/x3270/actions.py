#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "x3270-3.3"

def setup():
    autotools.configure("--without-pr3287 \
                         --with-x \
                         --without-icu \
                         --disable-dbcs \
                         --without-tcl")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/share/pixmaps", "x3270-icon2.xpm", "x3270.xpm")

    pisitools.dohtml("html")
    pisitools.dodoc("Examples")
