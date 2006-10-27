#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    ###Symlink setup /var/tmp/pisi/fluxconf-0.9.9-2/install/usr/bin/fluxbare
    pisitools.remove("/usr/bin/fluxbare")
    pisitools.remove("/usr/bin/fluxkeys")
    pisitools.remove("/usr/bin/fluxmenu")
    
    pisitools.dosym("/usr/bin/fluxconf", "/usr/bin/fluxbare")
    pisitools.dosym("/usr/bin/fluxconf", "/usr/bin/fluxkeys")
    pisitools.dosym("/usr/bin/fluxconf", "/usr/bin/fluxmenu")
    ###
    
    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "ChangeLog", "COPYING", "INSTALL", "docs/*", "NEWS", "README", "TODO")
