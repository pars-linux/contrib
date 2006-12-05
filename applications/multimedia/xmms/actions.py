#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("WANT_AUTOCONF", "2.5")
    shelltools.export("WANT_AUTOMAKE", "1.9")
    autotools.configure("--enable-alsa \
                         --enable-esd \
                         --enable-oss \
                         --enable-mikmod \
                         --with-libmikmod \
                         --enable-vorbis \
                         --enable-opengl \
                         --enable-cdaudio \
                         --enable-simd \
                         --enable-mpg123 \
                         --enable-ipv6")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "ChangeLog", "FAQ", "NEWS", "README", "TODO")
