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
    pisitools.dodoc("playonlinux/LICENCE", "playonlinux/CHANGELOG")

    # clean things
    pisitools.removeDir("/usr/share/playonlinux/src")
