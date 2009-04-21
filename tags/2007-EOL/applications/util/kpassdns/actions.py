#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

WorkDir="KpassDNS"

def install():
    pisitools.dobin("src/KpassDNS.py")
    pisitools.domo("po/tr.po", "tr", "KpassDNS.mo")
    pisitools.rename("/usr/bin/KpassDNS.py", "KpassDNS")
    pisitools.insinto("/usr/share/applications","src/KpassDNS.desktop")
    pisitools.insinto("/usr/share/pixmaps","src/KpassDNS.png")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "INSTALL", "README")
