#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import libtools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

WorkDir = "geos-3.0.0rc5"

def setup():
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

    pythonmodules.fixCompiledPy()

    pisitools.dodoc("AUTOHORS", "ChangeLog", "COPYING", "NEWS", "README", "TODO")
