#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="gnaural-0.4.20070301"

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.domo("po/gnaural.tr.po", "tr", "gnaural.mo")
    pisitools.insinto("/usr/share/pixmaps", "pixmaps/*")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "INSTALL", "NEWS", "README")
