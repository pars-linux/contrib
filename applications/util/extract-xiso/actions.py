#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

WorkDir = "extract-xiso"

def setup():
    pisitools.dosed("Makefile", "-O2", "%s" % get.CFLAGS())
    

def build():
    autotools.make()

def install():
    pisitools.dobin("extract-xiso")
    pisitools.dodoc("LICENSE.TXT", "README.TXT", "released_version_is_2.5")
