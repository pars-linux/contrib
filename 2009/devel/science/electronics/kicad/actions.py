#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


WorkDir = "kicad"

def build():
    autotools.make("-f makefile.gtk")

    shelltools.cd("kicad/minizip")
    autotools.make("-f makefile.unx")

def install():
    for exe in ["eeschema/eeschema","pcbnew/pcbnew","cvpcb/cvpcb","kicad/kicad",
                "kicad/minizip/minizip","gerbview/gerbview"]:
        pisitools.insinto("/usr/lib/kicad/linux", exe)

    for directory in ["library","internat","template","help","kicad/library/*",
                      "kicad/modules","kicad/template/*","kicad/help/*","kicad/demos"]:
        pisitools.insinto("/usr/lib/kicad", directory)

    pisitools.insinto("/usr/lib/kicad/linux/plugins","eeschema/plugins/netlist_form_pads-pcb")
    pisitools.insinto("/usr/share/pixmaps","kicad_icon.png","kicad.png")

    pisitools.dodoc("author.txt","copyright.txt","news.txt","contrib.txt","version.txt")
