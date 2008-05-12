#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir="marbles-1.0.0-1"

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.insinto("/usr/share/marbles/data", "src/data/*")
    pisitools.insinto("/usr/share/pixmaps", "src/data/Marbles_icon.png", "marbles.png")

    pisitools.domove("/usr/bin/marbles", "/usr/share/marbles")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
