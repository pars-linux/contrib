#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def build():
    shelltools.export("CC", "%s" % get.CC())
    shelltools.export("CFLAGS", "%s" % get.CFLAGS())
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.doman("jacklaunch.1")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "WORKING", "README")

    pisitools.remove("/usr/lib/libjackasyn.a")