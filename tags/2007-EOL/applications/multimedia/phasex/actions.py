#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
#
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

    pisitools.domove("usr/share/phasex/phasex.desktop", "usr/share/applications/")
    pisitools.dosym("/usr/share/phasex/pixmaps/phasex-icon.png", "/usr/share/pixmaps/phasex-icon.png")

    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README", "TODO")
