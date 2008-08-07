#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "%s-%s-src/%s-builder" % (get.srcNAME(), get.srcVERSION(), get.srcNAME())

def build():
    shelltools.export("JAVA_HOME", "/opt/sun-jre")
    shelltools.system("ant")

def install():
    pisitools.dobin("dist-bin/ganttproject.sh")
    pisitools.rename("/usr/bin/ganttproject.sh", "ganttproject")
    pisitools.insinto("/usr/share/ganttproject", "dist-bin/*")
    shelltools.chmod("../ganttproject/data/resources/icons/ganttproject.png", 644)
    pisitools.insinto("/usr/share/pixmaps", "../ganttproject/data/resources/icons/ganttproject.png")
    pisitools.remove("/usr/share/ganttproject/ganttproject.*")
