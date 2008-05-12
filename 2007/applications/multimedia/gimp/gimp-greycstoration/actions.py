#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "GREYCstoration-2.6"

def build():
    shelltools.cd("src")
    autotools.make("gimp")

def install():
    pisitools.insinto("/usr/lib/gimp/2.0/plug-ins/", "src/greycstoration4gimp")
