#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="commons-el-%s-src" % get.srcVERSION()

def setup():
    shelltools.export("LC_ALL", "C")
    shelltools.system("ant jar")

def install():
    pisitools.insinto("/usr/lib/java","dist/commons-el.jar","commons-el.jar")

    pisitools.dodoc("*.txt")
    pisitools.dohtml("*.html")
