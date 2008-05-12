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

WorkDir="commons-logging-%s-src" % get.srcVERSION()

def setup():
    shelltools.move("build.properties.sample", "build.properties")
    shelltools.system("ant -v compile")

def install():
    pisitools.insinto("/usr/share/java","target/commons-logging-api-*.jar","commons-logging-api.jar")
    pisitools.insinto("/usr/share/java","target/commons-logging-adapters-*.jar","commons-logging-adapters.jar")
    pisitools.insinto("/usr/share/java","target/commons-logging-1.1.jar","commons-logging.jar")

    pisitools.dodoc("README.txt")
    pisitools.dohtml("*.html")
