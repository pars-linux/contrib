#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir=""

def build():
    shelltools.cd("lib")
    autotools.make()
    shelltools.cd("../clit18")
    autotools.make()

def install():
    shelltools.cd("clit18")
    pisitools.dobin("clit")
    pisitools.dodoc("COPYING", "../README")
