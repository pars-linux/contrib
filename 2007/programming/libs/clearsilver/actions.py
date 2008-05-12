#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

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
                         --disable-perl \
                         --disable-ruby \
                         --disable-csharp")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # no static libs
    pisitools.remove("/usr/lib/*.a")

    pisitools.dodoc("CS_LICENSE", "LICENSE", "README*")
