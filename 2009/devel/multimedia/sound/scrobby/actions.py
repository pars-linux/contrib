#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("CXX", get.CXX())
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.removeDir("/usr/share/doc/scrobby")

    for i in ["cache", "log", "run"]:
        pisitools.dodir("/var/%s/scrobby" % i)

    pisitools.dodoc("AUTHORS", "COPYING")
