#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-nls \
                         --enable-rpath \
                         --enable-ipv6 \
                         --enable-chardet \
                         --disable-pulse \
                         --disable-coreaudio \
                         --disable-gconf \
                         --disable-gnomeshortcuts \
                         --disable-neon \
                         --enable-amidiplug \
                         --enable-amidiplug-alsa \
                         --disable-amidiplug-flysn \
                         --enable-amidiplug-dummy \
                         --with-sidplay2=/usr \
                         --with-sidplay2-lib=/usr/lib \
                         --with-sidplay2-inc=/usr/include/sidplay \
                         --with-sidbuilders=/usr \
                         --with-builders-inc=/usr/include/sidplay/builders \
                         --with-builders-lib=/usr/lib/sidplay/builders")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ChangeLog", "COPYING", "AUTHORS", "NEWS")
