#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.unlinkDir("apidocs")
    shelltools.unlink("resolver.jar")

def build():
    shelltools.system("ant -f resolver.xml jar")

def install():
    pisitools.insinto("/usr/share/java","build/*.jar")

    pisitools.dodoc("KEYS","LICENSE.resolver.txt","NOTICE-resolver.txt")

