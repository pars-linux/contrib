#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def setup():
    pisitools.dosed("fpm2.desktop", "fpm2/pixmaps/logo.png","pixmaps/fpm2.png")
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.insinto("/usr/share/pixmaps", "pixmaps/logo.png", "fpm2.png")
    pisitools.insinto("/usr/share/applications", "fpm2.desktop")
    pisitools.doman("fpm2.1")
    pisitools.dodoc("README", "AUTHORS", "Changelog", "COPYING")
