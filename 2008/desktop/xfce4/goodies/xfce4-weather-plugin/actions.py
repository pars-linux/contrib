#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-x")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dosym("/usr/share/xfce4/weather/icons/liquid/0.png", "/usr/share/pixmaps/xfce4-weather.png")

    pisitools.remove("/usr/share/icons/hicolor/icon-theme.cache")

    pisitools.dodoc("NEWS", "TODO", "AUTHORS", "ChangeLog")
