#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

imageDir = "/usr/lib/%s/site-packages/quodlibet/images" % get.curPYTHON()

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    for i in ["quodlibet.png", "exfalso.png"]:
        pisitools.dosym("%s/%s" % (imageDir, i), "/usr/share/pixmaps/%s" % i)

    pisitools.dodoc("COPYING", "HACKING", "NEWS", "README")
