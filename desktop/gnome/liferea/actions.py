#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.autoheader()
    autotools.autoconf()
    autotools.configure("--with-x  \
                                  --disable-sm \
                                  --disable-nm \
                                  --disable-lua \
                                  --enable-gtkhtml2 \
                                  --disable-xulrunner \
                                  --disable-gecko \
                                  --enable-gnutls \
                                  --enable-libnotify")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("NEWS", "README", "ChangeLog", "AUTHORS")
    # conflict
    pisitools.remove("/usr/share/icons/hicolor/icon-theme.cache")
