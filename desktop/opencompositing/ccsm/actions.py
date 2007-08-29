#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

WorkDir = "ccsm"

def install():
    pythonmodules.install("--prefix=/usr")

    # Turkish translation
    pisitools.domo("po/tr.po", "tr", "ccsm.mo")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "LICENSE")
