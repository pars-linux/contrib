#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    autotools.make()

def install():
    pisitools.dobin("wbar", "/usr/bin")
    pisitools.dodir("/usr/share/wbar")
    shelltools.copytree("iconpack", "%s/usr/share/wbar" % get.installDIR())
    pisitools.dosym("/usr/share/wbar/iconpack/comic.ttf", "/usr/share/wbar/iconpack/wbar.osx/font.ttf")
    shelltools.copy("dot.wbar", "%s/usr/share/wbar" % get.installDIR())
