#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools

def setup():
    autotools.aclocal()
    autotools.autoconf()
    autotools.automake()
    libtools.libtoolize("--copy --force")
    autotools.configure("--disable-static \
                         --disable-gtk-doc \
                         --enable-nautilus-extension=no")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "README", "NEWS", "ChangeLog")
