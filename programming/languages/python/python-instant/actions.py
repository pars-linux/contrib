#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "instant"

def install():
    pythonmodules.install()

    for i in ["makedoc.sh","maketarball.sh", "TODO"]:
        pisitools.remove("/%s/%s/%s/" % (get.docDIR(), get.srcTAG(), i))

    pisitools.dodoc("ChangeLog", "RELEASENOTES", "AUTHORS")
