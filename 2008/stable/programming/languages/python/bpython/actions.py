#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

WorkDir = get.srcNAME()

def install():
    pythonmodules.install()

    pisitools.doman("doc/bpython.1", "doc/bpythonrc.5")
    pisitools.dodoc("LICENCE", "CHANGES", "README", "sample-rc")

