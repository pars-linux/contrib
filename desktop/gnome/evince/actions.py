#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "evince-0.5.5"

def setup():
    shelltools.export("WANT_AUTOMAKE", "1.9")
    autotools.configure("--disable-scrollkeeper \
                         --enable-nautilus \
                         --enable-ps \
                         --enable-schemas-install \
                         --enable-tiff \
                         --disable-djvu \
                         --disable-dvi \
                         --enable-t1lib \
                         --enable-pixbuf \
                         --with-gconf-source=/etc/gconf/gconf.xml.defaults \
                         --with-gconf-schema-file-dir=/etc/gconf/schemas \
                         --enable-comics \
                         --enable-impress")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "Changelog", "COPYING", "NEWS", "README", "TODO")

