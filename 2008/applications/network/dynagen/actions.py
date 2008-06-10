#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def install():
    for data in ["dynagen","*.py"]:
        pisitools.insinto("/usr/lib/%s" % get.curPYTHON(), data)
    pisitools.dosym("/usr/lib/%s/dynagen" % get.curPYTHON(), "/usr/bin/dynagen")

    pisitools.dohtml("docs/*")
    pisitools.dodoc("COPYING", "README.txt")
