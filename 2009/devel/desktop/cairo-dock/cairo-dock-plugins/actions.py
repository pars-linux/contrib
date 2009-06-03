#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    # autotools.autoreconf("-isvf")
    autotools.configure("--disable-static \
                         --disable-old-gnome-integration \
                         --disable-gnome-integration \
                         --disable-xfce-integration \
                         --enable-alsa-mixer")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
