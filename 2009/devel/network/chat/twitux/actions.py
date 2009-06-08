#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--disable-static \
                         --enabe-spell \
                         --disable-scrollkeeper \
                         --enable-nls \
                         --enable-dbus=yes \
                         --enable-gnome-keyring")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dosym("/usr/share/icons/hicolor/48x48/apps/twitux.png", "/usr/share/pixmaps/twitux.png")

    pisitools.dodoc("AUTHORS", "NEWS", "README", "TODO", "ChangeLog", "COPYING")
