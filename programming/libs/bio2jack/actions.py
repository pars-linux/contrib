#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import libtools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="bio2jack"

def setup():
    shelltools.export("WANT_AUTOMAKE", "1.8")
    shelltools.export("WANT_AUTOCONF", "2.5")
    autotools.aclocal()
    autotools.automake()
    autotools.autoconf()
    libtools.libtoolize("--copy --force")
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("ChangeLog", "AUTHORS", "INSTALL*", "NEWS", "README*")

