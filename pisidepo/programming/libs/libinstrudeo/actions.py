#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools


def setup():
    shelltools.export("libxmlpp_CFLAGS","-I/usr/include/libxml++-1.0 -I/usr/lib/libxml++-1.0/include")
    shelltools.export("libxmlpp_LIBS","-L/usr/lib -lxml++-1.0")
    shelltools.system("/usr/bin/autoreconf")
    shelltools.system("/usr/bin/libtoolize --copy --force")
    autotools.configure()

def build():
    autotools.make()


def install():
    autotools.install()