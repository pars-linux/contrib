#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "TurquazLinux08Beta5"
NoStrip = "/"

def install():
    shelltools.unlinkDir(get.workDIR() + "/TurquazLinux08Beta5/java")

#   it works with comar
#   shelltools.system("chmod 777 -R %s/TurquazLinux08Beta5/turquaz/08Beta5/database" % get.workDIR())

    pisitools.dodir("/usr/share/pixmaps")
    shelltools.system('unzip -j %s/TurquazLinux08Beta5/turquaz/08Beta5/lib/turquaz-client.jar \
                       icons/turquaz_paw.gif -d %s/usr/share/pixmaps'
                       % (get.workDIR(), get.installDIR()) )
    pisitools.insinto("/opt/TurquazLinux08Beta5/", "turquaz/08Beta5/*")
    pisitools.remove("/opt/TurquazLinux08Beta5/database/turquaz.script")
    pisitools.domove("/opt/TurquazLinux08Beta5/turquaz.sh", "/usr/bin")

#   same as above
#   shelltools.chmod(get.installDIR() + "/opt/TurquazLinux08Beta5/database", 4777)
#   shelltools.chmod(get.installDIR() + "/opt/TurquazLinux08Beta5/database/", 0777)
#   shelltools.system("chmod 777 -R %s/opt/TurquazLinux08Beta5/database" % get.installDIR())

    pisitools.dodoc("install.txt", "yukleme.txt", "lisans/*")

