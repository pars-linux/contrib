#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "conversion_tools"

def install():
    pisitools.dosed("conver/Conversions.desktop", "~/.kde/share/apps/konqueror/servicemenus", "/usr/bin")
    pisitools.dosed("conver_submenus/Conversions_submenus.desktop", "~/.kde/share/apps/konqueror/servicemenus", "/usr/bin")

    pisitools.insinto("%s/share/apps/konqueror/servicemenus" % get.kdeDIR(), "conver/Conversions.desktop")
    pisitools.insinto("%s/share/apps/konqueror/servicemenus" % get.kdeDIR(), "conver_submenus/Conversions_submenus.desktop")

    pisitools.dobin("conver/conver.sh")
    pisitools.dobin("conver_submenus/conver_submenus.sh")
