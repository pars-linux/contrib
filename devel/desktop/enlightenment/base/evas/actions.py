#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "evas"

def setup():
    shelltools.system("./autogen.sh")
    autotools.configure("--enable-gl-x11 \
                         --enable-buffer \
                         --enable-software-x11 \
                         --enable-xrender-x11 \
                         --enable-software-sdl \
                         --enable-fb \
                         --enable-directfb \
                         --with-qtdir=%s \
                         --with-x \
                         --disable-static" % get.qtDIR())

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING*", "README")
