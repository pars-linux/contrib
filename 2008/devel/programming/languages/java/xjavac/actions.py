#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="xjavac-20041208"

def build():
    shelltools.system("ant jar -Dclasspath=/usr/share/ant-core/lib")

def install():
    pisitools.insinto("/usr/share/java","dist/*.jar")
