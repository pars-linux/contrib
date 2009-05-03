#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile", "-O -Wall -c", "-Wall -c %s" % get.CFLAGS())
    pisitools.dosed("Makefile", "-O -Wall -lfreeimage", "-Wall %s -lfreeimage" % get.LDFLAGS())
    pisitools.dosed("Makefile", "doc/\$\(PROGRAM\)", "doc/%s" % get.srcTAG())
    pisitools.dosed("Makefile", "/usr/local", "/usr")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/icons/hicolor/48x48/apps/", "data/icons/fotoxx.png")
