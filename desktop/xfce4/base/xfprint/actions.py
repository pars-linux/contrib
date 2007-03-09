#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir="xfprint-4.4.0"

def setup():
    autotools.configure("--enable-static=no \
                                  --enable-cups \
                                  --disable-bsdlpr")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("README", "TODO", "NEWS", "AUTHORS", "ChangeLog")
    # conflict
    pisitools.remove("/usr/share/icons/hicolor/icon-theme.cache")
