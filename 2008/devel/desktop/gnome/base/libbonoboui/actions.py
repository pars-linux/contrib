#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--disable-static \
                         --with-x")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("NEWS", "README", "ChangeLog", "INSTALL")
