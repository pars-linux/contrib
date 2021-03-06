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
    shelltools.export("CC", get.CC())
    shelltools.system("./autogen.sh")

    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dosym("/usr/share/xournal/pixmaps/xournal.png", "/usr/share/pixmaps/xournal.png")

    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "NEWS", "README")
