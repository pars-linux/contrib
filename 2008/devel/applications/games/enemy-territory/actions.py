#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="."

def setup():
    shelltools.system("sh et-linux-2.60.x86.run --noexec --target %s" % get.workDIR())

def install():
    pisitools.insinto("/opt/enemy-territory/etmain", "etmain/*")
    pisitools.insinto("/opt/enemy-territory/pb", "pb/*")
    pisitools.insinto("/opt/enemy-territory/Docs", "Docs/*")
    pisitools.insinto("/opt/enemy-territory", "openurl.sh")

    pisitools.dobin("bin/Linux/x86/et", "/opt/enemy-territory")
    pisitools.dobin("bin/Linux/x86/etded.x86", "/opt/enemy-territory")
    pisitools.dobin("bin/Linux/x86/et.x86", "/opt/enemy-territory")

    pisitools.dosym("/opt/enemy-territory/et", "/usr/bin/et")

    pisitools.insinto("/usr/share/pixmaps", "ET.xpm")

    pisitools.dodoc("CHANGES", "README")
