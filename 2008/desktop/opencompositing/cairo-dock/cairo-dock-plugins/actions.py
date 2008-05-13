#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    for package in shelltools.ls("."):
        shelltools.cd(package)
        autotools.autoreconf("-isvf")
        autotools.configure("--disable-static")
        shelltools.cd("../")

def build():
    for package in shelltools.ls("."):
        shelltools.cd(package)
        autotools.make("-j1")
        shelltools.cd("../")

def install():
    for package in shelltools.ls("."):
        shelltools.cd(package)
        autotools.rawInstall("DESTDIR=%s" % get.installDIR())
        shelltools.cd("../")
