#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("AT_M4DIR", "m4")
    autotools.autoconf()
    autotools.configure("--enable-gnomefe \
                         --enable-shm \
                         --disable-schemas-install \
                         --disable-scrollkeeper  \
                         --enable-openssl \
                         --enable-perl \
                         --enable-python \
                         --enable-tcltk \
                         --enable-mmx \
                         --enable-ipv6 \
                         --enable-dbus \
                         --enable-nls \
                         --enable-libsexy \
                         --enable-libnotify")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/include/xchat-gnome", "src/common/xchat-plugin.h")
    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "ChangeLog", "COPYING*", "INSTALL", "NEWS", "README", "TODO")
