#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import libtools

def setup():
    libtools.libtoolize("--force")
    autotools.configure("--enable-static=no \
                                  --with-xml-catalog=/etc/xml/docbook \
                                  --with-partial-db-dir=scrollkeeper \
                                  --enable-nls")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("README", "AUTHORS", "ChangeLog", "NEWS")