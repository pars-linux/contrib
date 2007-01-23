#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="ud1.0b1"

def build():
    shelltools.cd("src/")
    autotools.make()

def install():
    pisitools.insinto("/usr/share/uzakdiyarlar/bin", "src/ud")
    pisitools.dosym("/usr/share/uzakdiyarlar/area/area.lst", "/usr/share/uzakdiyarlar/bin/area.lst")
    
    pisitools.insinto("/usr/share/uzakdiyarlar/area", "area/*")
    shelltools.copytree("belgeler", "%s/usr/share/uzakdiyarlar" % get.installDIR())
    
    pisitools.dodir("/usr/share/uzakdiyarlar/gods")
    pisitools.dodir("/usr/share/uzakdiyarlar/player")
    pisitools.dodir("/usr/share/uzakdiyarlar/log")