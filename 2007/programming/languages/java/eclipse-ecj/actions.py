#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="."

def build():
    shelltools.system("ant")

def install():
    pisitools.insinto("/usr/share/java","ecj.jar","org.eclipse.jdt.core_3.3.1.v_780.jar")
    pisitools.dosym("/usr/share/java/org.eclipse.jdt.core_3.3.1.v_780.jar","/usr/share/java/eclipse-ecj.jar")

    pisitools.dohtml("about.html")
