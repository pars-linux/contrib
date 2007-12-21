#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools

def setup():
    autotools.configure("--with-wx-config=/usr/bin/wx-config-2.8 \
                         --enable-static=no")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.insinto("/usr/share/pixmaps", "src/appicon.xpm", "wxcam.xpm")

    pisitools.removeDir("/usr/doc")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
