#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "%s-%s-src/ganttproject-builder" % (get.srcNAME(), get.srcVERSION())

def build():
    shelltools.system("ant")

def install():
    pisitools.dobin("dist-bin/ganttproject.sh")
    pisitools.rename("/usr/bin/ganttproject.sh", "ganttproject")
    pisitools.insinto("/usr/share/ganttproject", "dist-bin/*")
    pisitools.insinto("/usr/share/pixmaps", "../ganttproject/data/resources/icons/ganttproject.png")
    pisitools.remove("/usr/share/ganttproject/ganttproject.*")
