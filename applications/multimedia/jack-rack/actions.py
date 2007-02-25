#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-desktop-inst --disable-gnome")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s JR_DESKTOP_PREFIX=/usr/share" % get.installDIR())

    pisitools.dodoc("BUGS", "ChangeLog", "AUTHORS", "THANKS", "TODO", "WISHLIST")

