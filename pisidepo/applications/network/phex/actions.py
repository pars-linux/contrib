#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Uğur Çetin <jnmbk@users.sourceforge.net>

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "phex_2.8.10.98"

def install():
    #turkish patch
    shelltools.system("zip -r phex.jar phex && rm -fr phex")

    pisitools.dodir("/usr/share/pixmaps")
    shelltools.system("unzip -j phex.jar phex/gui/resources/icons/phex/phex_wiz.gif -d %s/usr/share/pixmaps" % get.installDIR())
    pisitools.insinto("/opt/phex", "*")
    pisitools.remove("/opt/freemind/pisiBuildState")