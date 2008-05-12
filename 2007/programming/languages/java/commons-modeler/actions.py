#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="commons-modeler-%s-src" % get.srcVERSION()

def setup():
    shelltools.export("LC_ALL", "C")
    shelltools.copy("build.properties.sample", "build.properties")
    shelltools.system("ant dist")

def install():
    pisitools.insinto("/usr/share/java","dist/commons-modeler.jar","commons-modeler.jar")
#TODO:api-docs
    pisitools.dodoc("*.txt")
