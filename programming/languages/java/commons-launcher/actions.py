#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="commons-launcher"

def setup():
    shelltools.export("LC_ALL", "C")
    shelltools.system("ant dist")

def install():
    pisitools.insinto("/usr/lib/java","dist/bin/commons-launcher.jar","commons-launcher.jar")

    pisitools.dodoc("dist/*.txt")
#TODO:pisitools.dohtml("dist/docs/api/*.html")
