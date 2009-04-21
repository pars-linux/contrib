#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "TurquazLinux08Beta5"
NoStrip = "/"

def install():
    shelltools.unlinkDir("%s/TurquazLinux08Beta5/java" % get.workDIR())

    pisitools.dodir("/usr/share/pixmaps")
    shelltools.system('unzip -j %s/TurquazLinux08Beta5/turquaz/08Beta5/lib/turquaz-client.jar \
                       icons/turquaz_paw.gif -d %s/usr/share/pixmaps'
                       % (get.workDIR(), get.installDIR()) )

    pisitools.insinto("/opt/TurquazLinux08Beta5/", "turquaz/08Beta5/*")
    pisitools.domove("/opt/TurquazLinux08Beta5/turquaz.sh", "/usr/bin")

    pisitools.remove("/opt/TurquazLinux08Beta5/database/turquaz.script")
    pisitools.remove("/opt/TurquazLinux08Beta5/lib/asm.jar")

    pisitools.dodoc("lisans/*")
