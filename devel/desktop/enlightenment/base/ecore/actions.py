#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "ecore"

def setup():
    shelltools.system("./autogen.sh")
    autotools.configure("--disable-static \
                         --enable-ecore-txt \
                         --enable-ecore-x \
                         --enable-ecore-evas \
                         --enable-ecore-evas-software-buffer \
                         --enable-ecore-evas-software-x11 \
                         --enable-ecore-evas-xrender-x11 \
                         --enable-ecore-evas-opengl-x11 \
                         --enable-ecore-software-sdl \
                         --enable-ecore-evas-opengl-glew \
                         --enable-ecore-con \
                         --enable-openssl \
                         --enable-ecore-ipc \
                         --enable-ecore-config \
                         --enable-ecore-file \
                         --enable-ecore-job \
                         --enable-inotify \
                         --enable-poll \
                         --enable-curl \
                         --with-x")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING*", "README")
