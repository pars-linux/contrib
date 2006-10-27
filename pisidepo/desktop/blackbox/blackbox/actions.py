#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--sysconfdir=/etc/X11/blackbox")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
#   shelltools.system("echo "/usr/bin/blackbox" > %s/etc/X11/Sessions/blackbox" % get.installDIR())
    pisitools.dodoc("README*", "AUTHORS", "ChangeLog*", "COMPLIANCE", "INSTALL", "LICENSE", "RELNOTES", "TODO")
