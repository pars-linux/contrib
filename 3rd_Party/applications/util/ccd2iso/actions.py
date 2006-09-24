#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir = "ccd2iso"

def setup():
    #gcc -o ccd2iso src/ccd2iso.c
    autotools.configure()
    libtools.libtoolize("--copy --force")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
#   pisitools.dobin("ccd2iso")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "INSTALL", "README", "NEWS", "TODO")
