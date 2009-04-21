#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = "cuyo-2.~-1.1"

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "README", "ChangeLog", "COPYING")
    pisitools.remove("/usr/share/icons/hicolor/32x32/apps/cuyo.png")
    pisitools.remove("/usr/share/icons/hicolor/64x64/apps/cuyo.png")