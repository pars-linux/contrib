#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools

NoStrip = "/"

def setup():
    autotools.aclocal()
    autotools.autoconf()
    autotools.automake("--add-missing")
    libtools.libtoolize("--copy --force")

    autotools.configure("--with-x \
                         --disable-nm \
                         --disable-webkit \
                         --enable-gecko=xulrunner \
                         --enable-gnutls \
                         --enable-dbus \
                         --enable-libnotify \
                         --disable-schemas-install")

def build():
    autotools.make()

def install():
    autotools.install()

    # conflict
    pisitools.remove("/usr/share/icons/hicolor/icon-theme.cache")

    pisitools.dodoc("NEWS", "README", "ChangeLog", "AUTHORS")
