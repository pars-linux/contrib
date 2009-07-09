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
                         --disable-rpath \
                         --disable-sse2 \
                         --enable-ipv6 \
                         --enable-chardet \
                         --disable-esd \
                         --enable-pulse \
                         --disable-coreaudio \
                         --disable-gnomeshortcuts \
                         --enable-amidiplug \
                         --enable-amidiplug-alsa \
                         --enable-amidiplug-dummy")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING", "README*")
