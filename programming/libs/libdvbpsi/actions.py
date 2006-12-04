#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "libdvbpsi4-0.1.5"
def setup():
    autotools.configure("--enable-release")

def build():
    autotools.make()
    shelltools.system("doxygen doc/doxygen.conf")

def install():
    autotools.install()
#   autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "INSTALL", "libdvbpsi.spec", "NEWS", "README")        

