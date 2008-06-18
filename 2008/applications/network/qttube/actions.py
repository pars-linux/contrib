#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = "QtTube"

def install():
    pisitools.dobin("qttube")

    pisitools.insinto("/usr/share/QtTube/src", "src/*")
    pisitools.insinto("/usr/share/QtTube/data", "data/*.png")
    pisitools.insinto("/usr/share/applications/", "data/qttube.desktop")
    pisitools.insinto("/usr/share/pixmaps/", "data/qttube-48x48.png", "qttube.png")

    pisitools.dodoc("AUTHORS", "README", "LICENSE")
