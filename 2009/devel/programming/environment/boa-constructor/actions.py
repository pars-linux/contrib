#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import pythonmodules

def install():
    pisitools.insinto("/usr/lib/%s/site-packages/boa-constructor" % get.curPYTHON(), "*")

    pythonmodules.fixCompiledPy()

    pisitools.dodoc("README.txt", "Credits.txt", "Changes.txt", "Bugs.txt", "Docs/*")
