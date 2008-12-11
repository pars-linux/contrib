#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-artist-screen \
                         --enable-colors")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.removeDir("/usr/share/doc")

    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README", "doc/*.sample", "doc/ncmpc.lirc")
