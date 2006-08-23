#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Fethi Aymaz <fethi@linux-sevenler.org>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
#   autotools.install()
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
#   pisitools.domove("/usr/fake64/", "/usr/share/")
#   pisitools.dosym("/usr/share/fake64/bin/romloader", "/usr/bin/fake64")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "INSTALL", "NEWS", "README", "TODO")