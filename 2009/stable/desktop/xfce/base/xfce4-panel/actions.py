#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--enable-gtk-doc")

    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.remove("/usr/share/icons/hicolor/icon-theme.cache")
    # Panel config files are already in pardus-default-settings-xfce.
    pisitools.removeDir("/etc")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "HACKING", "NEWS", "README", "TODO")
