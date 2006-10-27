#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.


from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "fluxbox-1.0rc2"

def setup():
    autotools.configure()
    
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

#   default keys, init and menu configurations
    pisitools.insinto("/etc/fluxbox", "data/keys")
    pisitools.insinto("/etc/fluxbox", "data/init")
    pisitools.insinto("/etc/fluxbox", "data/menu")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "INSTALL", "NEWS", "README", "TODO", "data/READ*")