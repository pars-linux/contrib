#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "sidplay-%s" % get.srcVERSION()

def setup():
    shelltools.export("CXXFLAGS", "%s -D_GNU_SOURCE" % get.CXXFLAGS())
    shelltools.export("CFLAGS", get.CFLAGS())

    autotools.autoreconf("-fi")
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "TODO", "README")
