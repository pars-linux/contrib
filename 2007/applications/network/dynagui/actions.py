#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

WorkDir = "dynagui"

def install():
    for data in ["dynagui.py", "libs", "img"]:
        pisitools.insinto("/usr/share/dynagui", data)

    pisitools.dodoc("ChangeLog", "COPYING")
