#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools

WorkDir = "imageshack_upload"

def install():
    pisitools.insinto("/usr/kde/3.5/share/apps/konqueror/servicemenus", "imageshack.desktop")
    pisitools.insinto("/usr/kde/3.5/share/icons", "imageshack.png")
    pisitools.dobin("imageshack_upload", "/usr/bin")
    pisitools.dodoc("README")
