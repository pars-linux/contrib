#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
import os

WorkDir="tuxmath"

def setup():
    pisitools.dosed("Makefile", "INSTALL_DIR=", "INSTALL_DIR=%s" % get.installDIR())

def build():
    autotools.make()

def install():
    pisitools.dodir("/usr/bin")

    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("docs/*.txt")

    # Remove CVS dirs in installDir
    for root, dirs, files in os.walk(get.installDIR()):
        if "CVS" in root:
            pisitools.removeDir(root.split("install")[1])
