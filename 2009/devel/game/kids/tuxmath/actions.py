#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir='tuxmath_w_fonts-%s' % get.srcVERSION()

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/share/applications", "tuxmath.desktop")
    pisitools.dosym("/usr/share/tuxmath/images/icons/icon.png", "/usr/share/pixmaps/tuxmath.png")

    pisitools.dodoc("doc/COPYING.txt", "doc/TODO.txt", "doc/README*", "doc/OFL.txt", "doc/changelog")
