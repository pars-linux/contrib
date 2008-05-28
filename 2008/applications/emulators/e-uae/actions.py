#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "e-uae-%s-WIP4" % get.srcVERSION()

def setup():
    autotools.configure("--disable-dependency-tracking \
                         --disable-gtktest \
                         --disable-sdltest \
                         --enable-largefile \
                         --enable-aga \
                         --enable-cdtv \
                         --enable-cd32 \
                         --enable-cycle-exact-cpu \
                         --enable-compatible-cpu \
                         --enable-jit \
                         --enable-natmem \
                         --disable-noflags \
                         --enable-threads \
                         --enable-autoconfig \
                         --enable-scsi-device \
                         --enable-debugger \
                         --enable-state-saving \
                         --enable-enforcer \
                         --enable-action-replay \
                         --enable-ui \
                         --enable-audio \
                         --enable-fdi \
                         --with-zlib \
                         --with-sdl \
                         --without-sdl-sound \
                         --with-sdl-gfx \
                         --with-sdl-gl \
                         --with-libscg-prefix=/usr \
                         --with-libscg-includedir=/usr/include \
                         --with-libscg-libdir=/usr/lib \
                         --with-alsa \
                         --with-caps")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.rename("/usr/bin/uae", "e-uae")
    pisitools.rename("/usr/bin/readdisk", "e-readdisk")

    pisitools.dodoc("docs/*", "CHANGES", "ChangeLog", "COPYING", "README")
