#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools

WorkDir = "InChI-1-software-1-02-beta"

def build():
    shelltools.cd("cInChI/gcc_makefile")
    autotools.make()

def install():
    pisitools.insinto("/usr/bin", "cInChI/gcc_makefile/cInChI-1", "inchi")

    pisitools.dodoc("readme.txt", "LICENSE")
