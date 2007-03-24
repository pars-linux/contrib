#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import cmaketools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir = "sqliteman-0.99"

def setup():
    cmaketools.configure(installPrefix = "%s/usr" % get.installDIR())

def build():
    cmaketools.make()

def install():
    cmaketools.install()
    pisitools.dodoc("AUTHORS", "README", "VERSION", "COPYING")

