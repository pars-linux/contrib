#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    # conflict
    pisitools.remove("/usr/share/icons/hicolor/icon-theme.cache")

    # it's in xfdesktop package for default configuration
    pisitools.remove("/etc/xdg/xfce4/panel/panels.xml")

    pisitools.dodoc("README*", "NEWS", "HACKING", "ChangeLog", "AUTHORS")
