#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def install():
    files = ["*.py","codegen","edit_sizers","widgets", "locale", "res", "templates", "icons"]
    for file in files:
        pisitools.insinto("/usr/lib/%s/site-packages/%s" % (get.curPYTHON(),get.srcNAME()), file)

    pisitools.dosym("/usr/lib/%s/site-packages/%s/wxglade.py" % (get.curPYTHON(),get.srcNAME()), "/usr/bin/wxglade")

    pisitools.dohtml("docs/tutorial.html", "docs/html/*")
    pisitools.dodoc("*.txt", "docs/*.xt", "")
