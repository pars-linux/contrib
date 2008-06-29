#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="PIDA-%s" % get.srcVERSION()

def install():
    pythonmodules.install()
    pythonmodules.fixCompiledPy()

    pisitools.insinto("/usr/share/pixmaps","pida/resources/pixmaps/pida-icon.png","pida.png")

    pisitools.dohtml("docs/html/*")
    pisitools.dodoc("docs/txt/*","AUTHORS","CHANGELOG","COPYING","README")
