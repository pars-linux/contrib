#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    #Fix binary paths
    for i in ("doc/sound.txt", "qdvdauthor/qslideshow/dialogcreate.cpp", "qdvdauthor/dialogexecute.cpp", "qdvdauthor/dialogsetup.ui", "test/test_qstring/main.cpp"):
        pisitools.dosed("%s" % i, "usr/local/bin", "usr/bin")

    autotools.rawConfigure("--no-configurator \
                            --prefix=/usr \
                            --omit-qrender \
                            --omit-local-ffmpeg \
                            --build-qslideshow")

def build():
    autotools.make()

def install():
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())

    pisitools.insinto("/usr/share/applications", "qdvdauthor.desktop")
    pisitools.insinto("/usr/share/pixmaps", "qdvdauthor.png")

    pisitools.dodoc("CHANGELOG", "COPYING", "README", "TODO", "doc/*.txt")
    pisitools.remove("/usr/share/doc/%s/Cross-Compile*" % get.srcTAG())
