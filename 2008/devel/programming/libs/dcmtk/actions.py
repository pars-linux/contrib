#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    shelltools.export("CXXFLAGS", get.CXXFLAGS())
    shelltools.export("CFLAGS", get.CFLAGS())
    autotools.configure("--sysconfdir=/etc/dcmtk \
                         --with-private-tags")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    autotools.rawInstall("DESTDIR=%s" % get.installDIR(), "install-lib")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR(), "install-include")

    pisitools.domove("/usr/share/doc/dcmtk/", "/usr/share/doc/%s/" % get.srcTAG())

    pisitools.dodoc("CHANGES.354")
