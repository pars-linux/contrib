#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--enable-static=no \
                         --enable-man \
                         --with-x \
                         --with-gecko=firefox \
                         --with-search=basic")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("TODO", "README", "NEWS", "ChangeLog", "AUTHORS")
