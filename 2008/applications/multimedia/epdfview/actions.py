#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("epdfview.desktop", "icon_epdfview-24.png",  "icon_epdfview-48.png")
    autotools.configure("--disable-rpath \
                         --with-cups")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dosym("/usr/share/epdfview/pixmaps/icon_epdfview-48.png", "/usr/share/pixmaps/epdfview.png")

    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "NEWS*", "README*", "TODO*")

