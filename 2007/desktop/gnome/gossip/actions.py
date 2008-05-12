#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--enable-static=no \
                         --enable-dbus=yes \
                         --enable-libnotify \
                         --enable-galago=no \
                         --enable-telepathy=no \
                         --enable-aspell=no \
                         --disable-scrollkeeper \
                         --disable-schemas-install \
                         --with-x \
                         --with-backend=gnome")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("README", "AUTHORS", "ChangeLog", "NEWS", "CONTRIBUTORS")

    # conflict
    pisitools.remove("/usr/share/icons/hicolor/icon-theme.cache")
