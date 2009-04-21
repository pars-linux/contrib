#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

WorkDir = "wxPython-src-%s/wxPython" % get.srcVERSION()

def install():
    pythonmodules.install("WX_CONFIG=wx-config-2.8")
    pythonmodules.fixCompiledPy()

    pisitools.dodoc("docs/*", "docs/screenshots")
