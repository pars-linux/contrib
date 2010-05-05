#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    # checking for gnomeapplet module... no
    # configure: error: gnomeapplet Python module required to build glipper
    autotools.configure("--disable-scrollkeeper \
                         --disable-schemas-install")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "MAINTAINERS", "NEWS", "README")
