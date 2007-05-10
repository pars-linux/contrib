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

WorkDir="commons-beanutils-%s-src" % get.srcVERSION()

def setup():
    pisitools.echo("build.properties","commons-collections.jar=/usr/lib/java/commons-collections.jar")
    pisitools.echo("build.properties","commons-logging.jar=/usr/lib/java/commons-logging.jar")
    shelltools.system("ant jar")

def install():
    pisitools.insinto("/usr/lib/java","dist/commons-beanutils.jar","commons-beanutils.jar")

    pisitools.dodoc("README.txt")
    pisitools.dohtml("*.html")
