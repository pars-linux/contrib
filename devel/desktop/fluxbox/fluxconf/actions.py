#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--disable-rpath")

def build():
    autotools.make()

def install():
    autotools.install()

    for files in ("fluxbare", "fluxkeys", "fluxmenu"):
        pisitools.remove("/usr/bin/%s" % files)
        pisitools.dosym("/usr/bin/fluxconf", "/usr/bin/%s" % files)

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README*", "ABOUT*", "TODO")
