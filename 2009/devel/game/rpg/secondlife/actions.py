#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "SecondLife-i686-%s" % get.srcVERSION()

def install():
    pisitools.insinto("/opt/secondlife",  "*")
    # pisitools.dobin("secondlife")
    pisitools.insinto("/usr/share/pixmaps", "secondlife_icon.png", "secondlife.png")
    pisitools.dodoc("*.txt")
