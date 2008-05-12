#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
#
# Fahri Tuğrul Gürkaynak <ftugrul@gmail.com>

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile.in", "-lslang", "-lslang -lncurses")

    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dosym("/usr/lib/libnewt.so.0.52.1", "/usr/lib/libnewt.so.0.52")

    pisitools.remove("/usr/lib/libnewt.a")

    pisitools.dodoc("ChangeLog", "AUTHORS", "NEWS", "README*")

