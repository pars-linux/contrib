#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "imaj.at-%s" % get.srcVERSION()

def install():
    pisitools.dobin("imaj.at.upload.py")
    pisitools.dobin("sendss.py")

    pisitools.insinto("%s/share/apps/konqueror/servicemenus" % get.kdeDIR(), "*.desktop")

