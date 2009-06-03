#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="commons-pool-%s-src" % get.srcVERSION()

def setup():
    shelltools.unlink("commons-pool-%s.jar" % get.srcVERSION())
    shelltools.system("ant build-jar")

def install():
    pisitools.insinto("/usr/share/java","dist/*.jar","commons-pool.jar")

    pisitools.dodoc("README.txt","RELEASE-NOTES.txt","NOTICE.txt")
