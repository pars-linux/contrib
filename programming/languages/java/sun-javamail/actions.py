#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="mail"

def setup():
    shelltools.system("JAVA_PKG_STRICT=true ant -Djavaee.jar=/usr/share/java/activation.jar jar")

def install():
    pisitools.insinto("/usr/share/java","build/release/*.jar")
