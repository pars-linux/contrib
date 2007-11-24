#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir = "%s/Build" % get.srcNAME()

def setup():
    pisitools.dosed("Makefile", "PISI_KDEDIR", get.kdeDIR())
    pisitools.dosed("Makefile", "PISI_DESTDIR", get.installDIR())

def build():
    autotools.make()

def install():
    autotools.rawInstall()
