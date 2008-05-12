#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="commons-fileupload-%s" % get.srcVERSION()

def setup():
    shelltools.export("LC_ALL", "C")
    shelltools.system("ant -v dist")

def install():
    pisitools.insinto("/usr/share/java","dist/commons-fileupload-1.2rc3.jar","commons-fileupload.jar")

    pisitools.dodoc("*.txt")
#	java API-doc path not complete    
#    pisitools.dohtml("dist/docs/*")
