#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "etl-%s_20071011" % get.srcVERSION()

def setup():
    shelltools.system("./bootstrap")

    autotools.configure()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "README", "NEWS")
