#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.autoreconf()
    autotools.configure("--disable-schemas-install \
                         --disable-scrollkeeper \
                         --enable-gtk-doc")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.remove("/usr/share/icons/hicolor/icon-theme.cache")
    pisitools.remove("/usr/bin/gbf-*") #exists already in gnome-build

    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "ChangeLog", "COPYING", "FUTURE", "MAINTAINERS", "NEWS", "README", "ROADMAP", "THANKS", "TODO")
