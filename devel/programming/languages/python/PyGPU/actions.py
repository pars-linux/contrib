#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "PyGPU-%sa-11" % get.srcVERSION()

def install():
    pythonmodules.install()

    autotools.make("doc")

    pisitools.dohtml("doc/html/*")
    pisitools.dodoc("README.txt", "COPYRIGHT.txt")
