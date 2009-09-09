#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--disable-schemas-install \
                         --with-gnome \
                         --without-gda \
                         --without-gb \
                         --with-paradox \
                         --with-perl \
                         --with-python")

    pisitools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "BEVERAGES", "BUGS", "ChangeLog", "COPYING", "HACKING", "MAINTAINERS", "NEWS", "README")
