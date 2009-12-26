#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules

def setup():
    autotools.autoreconf("-fiv")
    autotools.configure("--disable-applet \
                         --enable-gnomeprint \
                         --enable-gnomeprintui \
                         --disable-gtksourceview \
                         --enable-wnck \
                         --disable-totem_plparser \
                         --enable-gtop \
                         --disable-nautilusburn \
                         --disable-mediaprofiles \
                         --enable-rsvg \
                         --disable-metacity \
                         --enable-gnomekeyring \
                         --disable-gnomedesktop \
                         --disable-bugbuddy \
                         --disable-evolution \
                         --disable-evolution_ecal \
                         --disable-evince")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("README", "NEWS", "ChangeLog", "AUTHORS")
