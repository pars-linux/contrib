#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("lib3ds/Makefile.in", "@CFLAGS@", "@CFLAGS@ -fPIC")

    autotools.configure("--disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dobin("examples/3ds2rib")
    pisitools.dobin("examples/player")
    pisitools.rename("/usr/bin/player", "lib3ds-player")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "INSTALL", "NEWS", "README", "TODO")