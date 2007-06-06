#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules

WorkDir="Mixminion-0.0.8alpha2"

def install():
    pythonmodules.install()
    pisitools.insinto("/etc","etc/*.conf")

    pisitools.dodoc("PKG-INFO", "README","doc/*.txt")
