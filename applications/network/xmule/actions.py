#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "xmule-1.13.7"

def setup():
    autotools.configure("--enable-debug \
                         --enable-optimize \
                         --enable-nls \
                         --disable-gtk")
def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.insinto("/usr/share/pixmaps/", "xmule.xpm")
    pisitools.insinto("/usr/share/applications/", "xmule.desktop")
    pisitools.dodoc("ChangeLog", "ChangeLog-UNSTABLE", "docs/*")
