#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

NoStrip = "/"

def setup():
    shelltools.export("MOZILLA_CFLAGS", "-I/usr/lib/MozillaFirefox/include -I/usr/lib/MozillaFirefox/include/xpcom -I/usr/lib/MozillaFirefox/include/string -I/usr/include/nspr -I/usr/lib/MozillaFirefox/include/gtkembedmoz -I/usr/lib/MozillaFirefox/include/webbrwsr -I/usr/lib/MozillaFirefox/include/dom -I/usr/lib/MozillaFirefox/include/pref -I/usr/lib/MozillaFirefox/include/necko")
    shelltools.export("MOZILLA_LIBS", "-Wl,-R/usr/lib/MozillaFirefox -L/usr/lib/MozillaFirefox -lxpcom -lplds4 -lplc4 -lnspr4 -lpthread -ldl")

    autotools.configure("--with-x \
                         --disable-nm \
                         --disable-lua \
                         --disable-gtkhtml2 \
                         --disable-xulrunner \
                         --enable-gecko=firefox \
                         --enable-gnutls \
                         --enable-dbus \
                         --enable-libnotify")

def build():
    autotools.make()

def install():
    autotools.install()

    # conflict
    pisitools.remove("/usr/share/icons/hicolor/icon-theme.cache")

    pisitools.dodoc("NEWS", "README", "ChangeLog", "AUTHORS")
