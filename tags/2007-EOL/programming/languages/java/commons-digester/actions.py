#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="commons-digester-%s-src" % get.srcVERSION()

def setup():
    shelltools.export("LC_ALL", "C")
    pisitools.echo("build.properties","root=/usr/share/java")
    pisitools.echo("build.properties","commons-beanutils.jar=/usr/share/java/commons-beanutils.jar")
    pisitools.echo("build.properties","commons-logging.jar=/usr/share/java/commons-logging.jar")
    shelltools.system("ant dist")

def install():
    pisitools.insinto("/usr/share/java","dist/*.jar","commons-digester.jar")

    pisitools.dodoc("dist/*.txt")
#	java API-doc path not complete    
#    pisitools.dohtml("dist/docs/*")

