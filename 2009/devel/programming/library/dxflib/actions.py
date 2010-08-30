#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="dxflib-%s-1.src" % get.srcVERSION()

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    pisitools.insinto("/usr/lib", "lib/*")
    pisitools.insinto("/usr/include/dxflib", "src/*.h")
