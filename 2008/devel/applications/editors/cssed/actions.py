#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dosym("/usr/share/cssed/pixmaps/cssed-icon.png", "/usr/share/pixmaps/cssed.png")

    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "README", "NEWS")
