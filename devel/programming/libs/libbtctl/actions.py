#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--disable-static \
                         --enable-mono=no")

def build():
    autotools.make("-j1")

def install():
    autotools.install()

    pisitools.dodoc("TODO", "README", "NEWS", "AUTHORS", "ChangeLog")
