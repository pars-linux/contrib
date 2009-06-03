#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-python \
                         --enable-gamin \
                         --enable-modplug \
                         --enable-mp4v2")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("NEWS", "TODO", "ChangeLog","AUTHORS")
    pisitools.dosym("/usr/share/man/man1/beep-media-player-2.1", "/usr/share/man/man1/bmp2.1")

    pisitools.domove("/usr/share/icons/hicolor/48x48/apps/bmpx.png", "/usr/share/pixmaps")
