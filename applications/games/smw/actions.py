#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006-2008  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "smw-%s" % get.srcVERSION()

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    pisitools.dobin("smw")
    pisitools.dobin("leveledit")

    pisitools.insinto("/usr/share/smw/gfx","gfx/*")
    pisitools.insinto("/usr/share/smw/sfx","sfx/*")
    pisitools.insinto("/usr/share/smw/maps","maps/*.map")
    pisitools.insinto("/usr/share/smw/music","music/*")
    pisitools.insinto("/usr/share/smw/tours","tours/*")

    pisitools.dohtml("README.html")
    pisitools.dodoc("WHATSNEW.txt", "README.txt")
