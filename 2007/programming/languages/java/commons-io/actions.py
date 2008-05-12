#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="commons-io-%s-src" % get.srcVERSION()

def setup():
    shelltools.export("LC_ALL", "C")
    shelltools.system("ant dist")

def install():
    pisitools.insinto("/usr/share/java","build/commons-io-1.3.2.jar","commons-io.jar")

    #install standard text files
    pisitools.dodoc("*.txt")
    
    #install javadocs
    shelltools.system("unzip build/commons-io-*-javadoc.jar -d javadoc")
    pisitools.insinto("/usr/share/doc/%s" % get.srcTAG(), "javadoc")
    
