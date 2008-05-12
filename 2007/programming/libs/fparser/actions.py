#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def build():
    autotools.make("shared")

def install():
    pisitools.insinto("/usr/lib", "lib/*")
    pisitools.insinto("/usr/include/fparser", "src/fparser.h")

    pisitools.dodoc("src/fparser.txt")
