#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="HawkNL1.70"

def setup():
    shelltools.move("makefile.linux", "makefile")

def build():
    autotools.make()

def install():
    pisitools.dodir("/usr/lib")
    pisitools.dodir("/usr/include")
    autotools.rawInstall("LIBDIR=%s/usr/lib INCDIR=%s/usr/include" % (get.installDIR(), get.installDIR()))
    pisitools.dodoc("samples/*")