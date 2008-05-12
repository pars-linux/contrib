#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "."

def build():
    autotools.make()
    shelltools.system("/opt/sun-jdk/bin/jar cmf META-INF/MANIFEST.MF logisim.jar com javax net org src")

def install():
    pisitools.insinto("/usr/share/logisim", "logisim.jar")

    pisitools.dodoc("COPYING.TXT")
    pisitools.insinto("%s/%s" % (get.docDIR(), get.srcTAG()), "doc/*")
