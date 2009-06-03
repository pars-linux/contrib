#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2005, TUBITAK/UEKAE
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.
#

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools


def setup():
    autotools.configure("--disable-static \
                         --with-apr-config=/usr/bin/apr-1-config \
                         --with-apu-config=/usr/bin/apu-1-config")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.insinto("/usr/share/pixmaps","src/res/bitmaps/rapidsvn_32x32.xpm","rapidsvn.xpm")