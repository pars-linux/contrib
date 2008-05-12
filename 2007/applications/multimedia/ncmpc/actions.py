#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("doc/Makefile.in", "srcTAG", "%s/samples" % get.srcTAG())
    pisitools.dosed("Makefile.in", "srcTAG", get.srcTAG())

    autotools.configure("--enable-mouse \
                         --enable-search-screen \
                         --enable-key-screen \
                         --enable-clock-screen")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.removeDir("/usr/share/ncmpc")
