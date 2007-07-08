#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="commons-codec-%s" % get.srcVERSION()

def setup():
    shelltools.export("LC_ALL", "C")
    shelltools.system("ant jar")
    shelltools.system("touch LICENSE.txt")
    
def install():
    pisitools.insinto("/usr/share/java","dist/commons-codec-1.3.jar","commons-codec.jar")
	
    pisitools.dodoc("LICENSE")

