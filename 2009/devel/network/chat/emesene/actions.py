#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

def install():
    
    # .desktop entry
    pisitools.insinto("/usr/share/applications", "misc/emesene.desktop")
    
    # icon
    pisitools.insinto("/usr/share/pixmaps", "emesene-logo.png", "emesene.png")

    # emesene script
    pisitools.insinto("/usr/share/emesene", "*")
    
    # license & translators
    pisitools.dodoc("COPYING", "docs/TRANSLATORS")

    # no need for setup.py
    pisitools.remove("/usr/share/emesene/setup.py")



