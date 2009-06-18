#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-gnome-thumbnailers \
                         --enable-exif \
                         --enable-pcre \
                         --enable-wallpaper-plugin \
                         --enable-uca-plugin \
                         --enable-tpa-plugin \
                         --enable-apr-plugin \
                         --with-volume-manager=hal")

    pisitools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "FAQ", "HACKING", "NEWS", "README", "THANKS", "TODO")
