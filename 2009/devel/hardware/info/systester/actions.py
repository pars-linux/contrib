#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

WorkDir = "systester-%s-src" % get.srcVERSION()

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    # autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dobin("systester")
    pisitools.insinto("/usr/share/systester/data", "images/*.png")
    pisitools.insinto("/usr/share/pixmaps", "images/generic.png", "systester.png")
    pisitools.dodoc("Authors", "Changelog", "COPYING", "gpl.txt")
