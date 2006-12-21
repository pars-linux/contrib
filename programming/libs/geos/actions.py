#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import libtools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "geos-3.0.0rc3"

def setup():
    shelltools.export("WANT_AUTOCONF", "2.5")
    libtools.libtoolize("--copy --force")
    autotools.configure("--with-pic \
                         --disable-static \
                         --enable-inline \
                         --enable-cassert \
                         --enable-swig \
                         --enable-python \
                         --enable-ruby")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTOHORS", "ChangeLog", "COPYING", "NEWS", "README", "TODO")