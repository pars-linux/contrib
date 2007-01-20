#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "vamps-%s" % get.srcVERSION()

def build():
    autotools.make()

def install():
    pisitools.dobin("play_cell/play_cell")
    pisitools.dobin("vamps/vamps")
    pisitools.dodoc("COPYING", "INSTALL")
