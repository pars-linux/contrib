#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--disable-gnome-thumbnailers \
                         --with-volume-manager=hal")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.domo("po/tr.po", "tr", "Thunar.mo")

    # conflict
    pisitools.remove("/usr/share/icons/hicolor/icon-theme.cache")

    pisitools.dodoc("TODO", "THANKS", "README", "HACKING", "FAQ", "AUTHORS", "ChangeLog")
