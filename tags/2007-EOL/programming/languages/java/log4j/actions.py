#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="logging-log4j-%s" % get.srcVERSION()

def setup():
    shelltools.export("LC_ALL", "C")
    shelltools.system("ant jar")

def install():
    pisitools.insinto("/usr/share/java","dist/lib/log4j*.jar","log4j.jar")

    pisitools.dodoc("LICENSE")
    pisitools.dodoc("NOTICE")
    pisitools.dohtml("docs/*")
