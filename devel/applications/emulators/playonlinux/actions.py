#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2008  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "."
NoStrip = "/"

datadir = "/usr/share"

def install():
    pisitools.dodir(datadir)
    shelltools.copytree("playonlinux", "%s/%s/" % (get.installDIR(), datadir))

    pisitools.dobin("playonlinux/playonlinux")
    pisitools.domo("playonlinux/lang/po/tr.po", "tr", "pol.mo")
    pisitools.domove("/usr/share/locale/tr", "/usr/share/playonlinux/lang/locale/")

    pisitools.dodoc("playonlinux/LICENCE", "playonlinux/CHANGELOG")

    # clean things
    pisitools.removeDir("/usr/share/playonlinux/src")
    pisitools.removeDir("/usr/share/locale")
    pisitools.removeDir("/usr/share/playonlinux/lang/po")
    pisitools.remove("/usr/share/playonlinux/LICENCE")
    pisitools.remove("/usr/share/playonlinux/CHANGELOG")
