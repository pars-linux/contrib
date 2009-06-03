#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--disable-static \
                         --enable-sound-settings \
                         --enable-xsettings-daemon \
                         --enable-libnotify \
                         --enable-libxklavier \
                         --enable-xcursor")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.remove("/etc/xdg/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml")

    pisitools.dodoc("README", "NEWS", "TODO", "AUTHORS", "ChangeLog")
