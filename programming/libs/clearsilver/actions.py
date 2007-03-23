#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-compression \
                         --enable-remote-debugger \
                         --with-zlib \
                         --enable-gettext \
                         --enable-apache \
                         --enable-wdb \
                         --enable-python \
                         --enable-perl \
                         --disable-ruby \
                         --disable-csharp")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("CS_LICENSE", "LICENSE", "INSTALL", "README*")
