#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "wxGTK-%s" % get.srcVERSION()
wxprefix = "/usr/wx/2.8"

def setup():
    # it fails if ODBC is enabled when using unicode
    autotools.rawConfigure("--prefix=%s \
                            --with-libpng \
                            --with-libjpeg \
                            --with-libtiff \
                            --with-libxpm \
                            --with-expat \
                            --with-regex \
                            --with-gtk=2 \
                            --without-gnomeprint \
                            --without-gnomevfs \
                            --without-odbc \
                            --with-opengl \
                            --with-sdl \
                            --enable-sound \
                            --enable-joystick \
                            --disable-accessibility \
                            --disable-compat24 \
                            --enable-compat26 \
                            --enable-unicode \
                            --enable-xrc" % wxprefix)

def build():
    autotools.make()
    autotools.make("-C contrib")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    autotools.rawInstall("DESTDIR=%s -C contrib" % get.installDIR())

    pisitools.dosym("%s/lib/wx/config/gtk2-unicode-release-2.8" % wxprefix, "/usr/bin/wx-config-2.8")
    pisitools.dosym("%s/bin/wxrc-2.8" % wxprefix, "/usr/bin/wxrc-2.8")

    pisitools.dodoc("docs/*.txt", "docs/*.htm")
