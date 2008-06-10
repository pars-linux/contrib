#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
#

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def install():
    pisitools.dobin("cream")

    for data in ["addons","bitmaps","docs","docs-html","filetypes","help","lang","*.vim","creamrc"]:
        pisitools.insinto("/usr/share/vim/vim71/cream",data)

    pisitools.insinto("/usr/share/applications/","cream.desktop")
    pisitools.insinto("/usr/share/icons/","cream.png")
