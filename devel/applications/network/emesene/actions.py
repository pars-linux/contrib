#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules

WorkDir = "emesene-rc"

def install():
    pythonmodules.install()

    pisitools.insinto("/usr/bin", "emesene.bin", "emesene")

    pisitools.dodoc("COPYING", "docs/TRANSLATORS")
