#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="edb-1.0.5.007"

def setup():
    autotools.configure("--enable-compat185 \
                         --enable-dump185 \
                         --disable-bigfile \
                         --disable-gtk \
                         --disable-test \
                         --enable-ncurses")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "COPYING*", "README*")