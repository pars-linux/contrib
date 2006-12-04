#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="imlib2_loaders-1.2.2.001"

def setup():
    shelltools.export("IMLIB2_CONFIG", "")
    shelltools.export("EDB_CONFIG", "")
    shelltools.export("EET_CONFIG", "")
    autotools.configure("--enable-edb \
                         --enable-eet \
                         --enable-xcf")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README*")