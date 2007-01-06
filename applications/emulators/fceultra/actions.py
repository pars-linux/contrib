#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir = "fceu"

def setup():
    autotools.configure("--with-opengl \
                         --disable-sdltest")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "TODO", "Documentation/*")
    pisitools.insinto("/usr/share/doc/%s" % get.srcTAG(), "Documentation/tech")

