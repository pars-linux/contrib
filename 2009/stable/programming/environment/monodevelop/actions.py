#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--disable-update-mimedb \
                         --disable-update-desktopdb")

def build():
    shelltools.export("MONO_SHARED_DIR",".")

    autotools.make("-j1")

def install():
    shelltools.export("MONO_SHARED_DIR",".")

    autotools.install()

    pisitools.remove("/usr/share/icons/hicolor/icon-theme.cache")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
