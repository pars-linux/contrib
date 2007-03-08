#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "sqliteman-0.99"

def setup():
    shelltools.system("cmake .")

def build():
    autotools.make()

def install():
    pisitools.dobin("sqliteman/sqliteman/sqliteman")
    pisitools.insinto("/usr/share/pixmaps", "sqliteman/sqliteman/icons/sqliteman.png")
    pisitools.dodoc("AUTHORS", "README", "VERSION", "COPYING")

