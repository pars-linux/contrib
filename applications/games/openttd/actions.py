#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir = "openttd-0.5.3-RC3"

def setup():
    #dummy configure enables freetype
    autotools.rawConfigure()

def build():
    autotools.make("BINARY_DIR=usr/share/openttd \
                    DATA_DIR=usr/share/openttd \
                    INSTALLDIR=usr/share/openttd \
                    USE_HOMEDIR=1 \
                    PERSONAL_DIR=.openttd \
                    INSTALL=1")

def install():
    pisitools.insinto("/usr/share/openttd/data", "data/*")
    pisitools.insinto("/usr/share/openttd/lang", "lang/*.lng")

    pisitools.doexe("openttd", "/usr/share/openttd")

    pisitools.dodoc("docs/*", "*.txt", "COPYING")
    #remove unneeded Readmes
    pisitools.remove("/usr/share/doc/%s/Readme_*" % get.srcTAG())

    #copy icons
    iconSizes = ["16", "32", "48", "64", "128", "256"]
    for size in iconSizes:
        pisitools.insinto("/usr/share/icons/hicolor/%sx%s/apps" % (size, size), "media/openttd.%s.png" % size, destinationFile = "openttd.png")
