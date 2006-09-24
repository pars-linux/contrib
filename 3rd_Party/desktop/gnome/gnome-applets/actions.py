#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    autotools.automake()
    autotools.configure("--with-x \
                         --with-gstreamer=0.10  \
                         --disable-battstat  \
                         --enable-flags  \
                         --enable-hal   \
                         --enable-ipv6  \
                         --disable-scrollkeeper")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # make docs for all applets

    pisitools.dodoc("ChangeLog", "AUTHORS", "INSTALL*", "NEWS", "README*")
