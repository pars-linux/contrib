#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "TurquazLinux08Beta5"
NoStrip = "/"

def install():
    shelltools.unlinkDir(get.workDIR() + "/TurquazLinux08Beta5/java")

    pisitools.dodir("/usr/share/pixmaps")
    shelltools.system('unzip -j %s/TurquazLinux08Beta5/turquaz/08Beta5/lib/turquaz-client.jar \
                       icons/turquaz_paw.gif -d %s/usr/share/pixmaps'
                       % (get.workDIR(), get.installDIR()) )
    pisitools.insinto("/opt/TurquazLinux08Beta5/", "turquaz/08Beta5/*")
    pisitools.remove("/opt/TurquazLinux08Beta5/database/turquaz.script")
    pisitools.remove("/opt/TurquazLinux08Beta5/lib/asm-3.0.jar")
    pisitools.domove("/opt/TurquazLinux08Beta5/turquaz.sh", "/usr/bin")
    pisitools.dodoc("install.txt", "yukleme.txt", "lisans/*")
