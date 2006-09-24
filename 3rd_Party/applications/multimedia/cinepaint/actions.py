#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

#WorkDir = "cinepaint-0.21-1"

def setup():
    autotools.configure("--with-openexr-prefix=/usr")
    

def build():
    autotools.make()
  
def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/share/pixmaps", "cinepaint.png")
    pisitools.insinto("/usr/share/applications", "cinepaint.desktop")
    pisitools.dodoc("README", "AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "tips.txt")
