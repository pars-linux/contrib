#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools


def setup():
    autotools.configure()
            
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())


#   default menu keys and other configureations for icewm
    pisitools.insinto("/etc/icewm", "lib/keys")
    pisitools.insinto("/etc/icewm", "lib/menu")
    pisitools.insinto("/etc/icewm", "lib/preferences")
    pisitools.insinto("/etc/icewm", "lib/toolbar")
    pisitools.insinto("/etc/icewm", "lib/winoptions")

    pisitools.dodoc("AUTHORS", "BUGS", "CHANGES", "COPYING", "INSTALL", "PLATFORMS", "README", "README.wm-session", "TODO", "VERSION")
    pisitools.dohtml("doc/*.html")
