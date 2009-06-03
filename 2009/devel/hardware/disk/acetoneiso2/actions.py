#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "acetoneiso2/src"

def setup():
    pisitools.dosed("acetoneiso2.pro", "/usr/share/apps/konqueror/servicemenus", "%s/%s/%s" % (get.installDIR(), get.kdeDIR(), "share/apps/konqueror/servicemenus"))
    pisitools.dosed("acetoneiso2.pro", "/usr/share/apps/d3lphin/servicemenus", "%s/%s/%s" % (get.installDIR(), get.kdeDIR(), "share/apps/dolphin/servicemenus"))

    paths = ["/usr/bin", "/usr/share/applications", "/usr/share/pixmaps", "/opt/acetoneiso"]

    for path in paths:
        pisitools.dosed("acetoneiso2.pro", path, "%s/%s" % (get.installDIR(), path))

    shelltools.system("qmake-qt4")

def build():
    autotools.make()

def install():
    autotools.install()
