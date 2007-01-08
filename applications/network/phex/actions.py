#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "phex_3.0.0.99"

def install():
    pisitools.dodir("/usr/share/pixmaps")
    shelltools.system("unzip -j lib/phex.jar phex/gui/resources/icons/phex/phex_wiz.gif -d %s/usr/share/pixmaps" % get.installDIR())
    pisitools.insinto("/opt/phex", "*")

