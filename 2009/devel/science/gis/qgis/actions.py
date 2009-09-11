#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "qgis_%s" % get.srcVERSION()

def setup():
    cmaketools.configure()

def build():
    cmaketools.make()

def install():
    cmaketools.install("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/pixmaps", "images/icons/qgis-icon.png", "qgis.png")

    pisitools.domove("/usr/man", "/usr/share")

    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "COPYING", "NEWS", "README", "TODO", "*.txt")
