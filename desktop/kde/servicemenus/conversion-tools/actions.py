#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools

WorkDir = "conversion_tools"

def install():
    pisitools.insinto("/usr/kde/3.5/share/apps/konqueror/servicemenus", "conver/Conversions.desktop")
    pisitools.insinto("/usr/kde/3.5/share/apps/konqueror/servicemenus", "conver_submenus/Conversions_submenus.desktop")
    pisitools.dobin("conver/conver.sh", "/usr/kde/3.5/share/apps/konqueror/servicemenus")
    pisitools.dobin("conver_submenus/conver_submenus.sh", "/usr/kde/3.5/share/apps/konqueror/servicemenus")
