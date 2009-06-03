#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "ogdi-3.2.0.beta1"

def setup():
    shelltools.export("TOPDIR", "%s/%s" % (get.workDIR(), WorkDir))
    autotools.configure("--with-zlib \
                         --with-proj \
                         --with-expat")

def build():
    shelltools.export("LD_LIBRARY_PATH", "%s/%s/bin/linux" % (get.workDIR(),get.srcDIR()))
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("ChangeLog", "LICENSE", "NEWS", "README", "VERSION")


