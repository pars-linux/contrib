#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-unicode=yes \
                         --enable-clock=yes \
                         --with-taglib=yes \
                         --with-curl=yes")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.removeDir("usr/share/doc")

    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "NEWS", "doc/config", "doc/keys")
