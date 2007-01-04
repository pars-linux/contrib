#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def install():
    pythonmodules.install()

    pisitools.insinto("/usr/share/doc/%s/examples" % get.srcTAG(), "examples/*")
    pisitools.dodoc("AUTHORS", "COPYING", "PKG-INFO", "TODO", "README")
