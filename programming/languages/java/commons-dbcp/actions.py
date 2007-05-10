#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    pisitools.echo("build.properties","commons-collections.jar=/usr/lib/java/commons-collections.jar")
    pisitools.echo("build.properties","commons-pool.jar=/usr/lib/java/commons-pool.jar")
    shelltools.system("ant build-jar")

def install():
    pisitools.insinto("/usr/lib/java","dist/*.jar","commons-dbcp.jar")

    pisitools.dodoc("README.txt")

