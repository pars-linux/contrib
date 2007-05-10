#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="apache-tomcat-5.5.23-src/servletapi"

def setup():
    shelltools.export("LC_ALL", "C")
    shelltools.system("ant -f jsr154/build.xml dist")
    shelltools.system("ant -f jsr152/build.xml dist")

def install():
    pisitools.insinto("/usr/lib/java","jsr154/dist/lib/servlet-api*.jar","servlet-api.jar")
    pisitools.insinto("/usr/lib/java","jsr152/dist/lib/jsp-api*.jar","jsp-api.jar")

    pisitools.dodoc("jsr154/dist/README.txt")
    pisitools.dodoc("jsr154/dist/LICENSE")
