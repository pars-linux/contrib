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
    pisitools.dodoc("README*", "NEWS", "HACKING", "ChangeLog", "AUTHORS")
    # conflict
    pisitools.remove("/usr/share/icons/hicolor/icon-theme.cache")
    pisitools.remove("/usr/share/icons/hicolor/48x48/apps/xfce-filemanager.png")