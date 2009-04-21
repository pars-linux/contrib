#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="commons-dbcp-%s-src" % get.srcVERSION()

def setup():
    shelltools.export("LC_ALL", "C")
    pisitools.echo("build.properties","commons-collections.jar=/usr/share/java/commons-collections.jar")
    pisitools.echo("build.properties","commons-pool.jar=/usr/share/java/commons-pool.jar")
    #for generics support
    pisitools.echo("build.properties","javac.source=1.5")
    
    #build jar file
    shelltools.system("ant build-jar")
    #build javadocs
    shelltools.system("ant javadoc");

def install():
    pisitools.insinto("/usr/share/java","dist/*.jar","commons-dbcp.jar")

    pisitools.dodoc("README.txt")
    pisitools.dodoc("LICENSE.txt")
    pisitools.dodoc("NOTICE.txt")
    pisitools.dodoc("RELEASE-NOTES.txt")
    #install javadocs
    pisitools.insinto("/usr/share/doc/%s" % get.srcTAG(), "dist/docs/api", "javadoc")
