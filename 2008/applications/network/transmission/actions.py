#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--disable-static \
                         --enable-gtk \
                         --enable-cli \
                         --enable-daemon")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.remove("/usr/share/icons/hicolor/icon-theme.cache")

    pisitools.dodoc("LICENSE", "COPYING", "AUTHOR", "README", "ChangeLog", "NEWS")
