#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-static \
                         --disable-xmms2 \
                         --disable-bmpx \
                         --enable-rss \
                         --disable-audacious \
                         --disable-mpd \
                         --disable-debug \
                         --enable-own-window \
                         --enable-proc-uptime \
                         --enable-hddtemp \
                         --enable-imlib2 \
                         --enable-portmon \
                         --enable-x11 \
                         --enable-double-buffer \
                         --enable-xdamage \
                         --enable-wlan \
                         --enable-xft")

def build():
    autotools.make()

def install():
    autotools.install()

    for data in ["doc/*.sample","extras/vim","extras/nano"]:
        pisitools.insinto("/usr/share/doc/%s/examples/" % get.srcTAG(), data)

    pisitools.dohtml("doc/*.html")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
