#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir = "%s/Build" % get.srcDIR()

def setup():
    pisitools.dosed("Makefile", "KDEDIR = /usr/", "KDEDIR = %s" % get.installDIR() + get.kdeDIR())

def build():
    autotools.make("all")

def install():
    autotools.rawInstall()

