#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.rawConfigure("--prefix=/usr \
                            --qt-dir=/usr/qt/3 \
                            --build-qplayer \
                            --build-qslideshow")
def build():
    autotools.make()

def install():
    for bins in ["bin/qdvdauthor", "bin/qplayer", "bin/qrender", "bin/qslideshow", "bin/to_pal_dvd.sh"]:
        pisitools.dobin(bins)
    #check whether to_pal_dvd.sh is necessary in the code above.. And also qrender does not enter the package.. Take care of this, check if it creates any problems. (it seems not creating any problem for now..) 

    pisitools.insinto("/usr/share/applications", "qdvdauthor.desktop")
    pisitools.insinto("/usr/share/pixmaps", "qdvdauthor.png")

    pisitools.dohtml("doc/html/en/*.html")
    pisitools.dodoc("CHANGELOG", "COPYING", "README", "TODO")
