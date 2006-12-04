#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = "proj-4.5.0"

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.insinto("/usr/include", "src/*.h")
    pisitools.dodoc("AUTHOR", "ChangeLog", "COPYING", "NEWS", "README")


