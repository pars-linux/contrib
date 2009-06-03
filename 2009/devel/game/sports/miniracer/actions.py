#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def build():
    autotools.make()

def install():
    pisitools.dobin("miniracer")

    pisitools.insinto("/usr/share/MiniRacer", "engine.glx")
    pisitools.insinto("/usr/share/MiniRacer/data", "data/pak0.pak")
    pisitools.insinto("/usr/share/MiniRacer/data", "data/config.cfg")
    pisitools.insinto("/usr/share/MiniRacer/data", "data/maps/*.bsp")
    pisitools.insinto("/usr/share/MiniRacer/data", "data/maps/maps1.lst")

    pisitools.doman("miniracer.6")

    pisitools.dodoc("AUTHORS", "CREDITS", "COPYING", "ChangeLog", "README")
