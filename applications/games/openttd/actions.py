#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = "openttd-0.5.0-RC1"

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
    pisitools.insinto("/usr/share/pixmaps", "media/openttd.128.png")
    pisitools.doexe("openttd", "/usr/share/openttd")
    pisitools.dodoc("docs/*", "*.txt")
    #remove unneeded Readmes
    pisitools.remove("/usr/share/doc/openttd-0.5.0_rc1-6/Readme_*")

