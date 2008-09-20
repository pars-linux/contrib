#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007,2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("setup.py", "share/doc/bkchem", "share/doc/%s" % get.srcTAG())

    pisitools.dosed("bkchem/oasa/oasa/config.py", "/home/beda/bin/cInChI-1-102b", "/usr/bin/inchi")

def install():
    pythonmodules.install("--prefix=/usr --strip=%s" % get.installDIR())

    pisitools.insinto("/usr/share/pixmaps", "images/bkchem.png")
