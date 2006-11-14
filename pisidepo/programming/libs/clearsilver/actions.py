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
                         --enable-gettext \
                         --enable-wdb \
                         --enable-python \
                         --enable-perl \
                         --enable-ruby \
                         --enable-csharp")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #install ruby files
    pisitools.insinto("/usr/lib/ruby/1.8/i686-linux", "ruby/ext/hdf/*.so")
    pisitools.insinto("/usr/lib/ruby/1.8", "ruby/lib/*.rb")

    pisitools.dodoc("CS_LICENSE", "LICENSE", "INSTALL", "README*")

    #no static libs
    pisitools.remove("/usr/lib/*.a")