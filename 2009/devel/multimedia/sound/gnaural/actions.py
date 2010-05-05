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
    shelltools.system("./autogen.sh")
    autotools.configure("--disable-rpath")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.domo("po/gnaural.tr.po", "tr", "gnaural.mo")
    pisitools.insinto("/usr/share/pixmaps", "pixmaps/*")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
