#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "imageshack_upload"

def install():
    pisitools.insinto("%s/share/apps/konqueror/servicemenus" % get.kdeDIR(), "imageshack.desktop")
    pisitools.insinto("%s/share/icons" % get.kdeDIR(), "imageshack.png")
    pisitools.dobin("imageshack_upload")
    pisitools.dodoc("README")
