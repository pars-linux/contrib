#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="xerces-2_9_1"

def build():
    shelltools.system("ant jar deprecatedjar")

def install():
    pisitools.insinto("/usr/share/java/", "build/*.jar")

    pisitools.dohtml("*.html")
    pisitools.dodoc("LICENSE", "README", "NOTICE", "*.txt", "docs/*")
