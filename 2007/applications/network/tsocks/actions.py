#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="tsocks-1.8"

def setup():
    autotools.configure("--libdir=/usr/lib")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # add new executable
    pisitools.dobin("validateconf")
    pisitools.dobin("saveme")
    pisitools.dobin("inspectsocks")

    # add simple conf file
    pisitools.insinto("/etc/socks","tsocks.conf.simple.example","tsocks.conf")

    # add doc and complex conf
    pisitools.dodoc("README*","FAQ","tsocks.conf.simple.example")
