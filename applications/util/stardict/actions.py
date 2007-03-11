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
    autotools.configure("--disable-gnome-support")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.remove("usr/share/pixmaps/stardict.png")
    pisitools.remove("usr/share/stardict/pixmaps/docklet_scan.png")
    pisitools.remove("usr/share/stardict/pixmaps/docklet_stop.png")
    pisitools.remove("usr/share/stardict/pixmaps/docklet_normal.png")
    pisitools.domo("po/tr.po" , "tr" , "stardict.mo")
    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "ChangeLog", "COPYING", "HowToCreateDictionary", "INSTALL", "NEWS", "README", "TODO")