#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir = "sqlitebrowser"

def setup():
    pisitools.dosed("Makefile", "/Developer/qt", get.qtDIR())

def build():
    autotools.make()

def install():
    pisitools.dobin("sqlitebrowser/sqlitebrowser")

