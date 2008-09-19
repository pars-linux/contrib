#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

WorkDir = "%s-3.0.0b6" % get.srcNAME()

def install():
    pythonmodules.install()

    pisitools.dohtml("documentation/*")
