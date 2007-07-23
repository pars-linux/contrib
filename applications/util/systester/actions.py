#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

WorkDir = "systester-%s-src" % get.srcVERSION()

def setup():
    shelltools.system("qmake")

def build():
    autotools.make()

def install():
    pisitools.dobin("systester")
    pisitools.insinto("/usr/share/systester/data", "images/*.png")

    pisitools.dodoc("gpl.txt")
