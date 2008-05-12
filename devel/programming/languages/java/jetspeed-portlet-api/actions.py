#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="jetspeed-2.1-src/portlet-api"

def setup():
    shelltools.system("mkdir class")
    shelltools.system("javac -sourcepath src/java src/java/javax/portlet/*.java -d class")
    shelltools.system("jar cvf portlet-api.jar -C class/ .")
    pisitools.echo("manifest","Specification-Title: Java Portlet API")
    pisitools.echo("manifest","Specification-Version: 1.0")
    shelltools.system("jar cvfm portlet-api.jar manifest -C class/ .")

def install():
    pisitools.insinto("/usr/share/java","portlet-api.jar","portlet-api.jar")

    pisitools.dodoc("changes.txt")
    pisitools.dohtml("docs/*")
