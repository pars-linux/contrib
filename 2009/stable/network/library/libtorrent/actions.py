#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "libtorrent-rasterbar-%s" % get.srcVERSION()

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static \
                         --enable-python-binding \
                         --with-zlib=system \
                         --with-asio=system \
                         --with-libgeoip=system \
                         --with-encryption=on \
                         --with-dht=on \
                         --with-ssl ")

def build():
    autotools.make("CXX=%s" % get.CXX())

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto('/usr/include/libtorrent/asio/', 'include/libtorrent/asio/*')
    pisitools.removeDir("/usr/bin")

    pisitools.dohtml("docs/*")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
