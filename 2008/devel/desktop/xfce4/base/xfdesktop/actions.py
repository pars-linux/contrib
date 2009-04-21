#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-static \
                         --enable-desktop-icons \
                         --enable-thunarx \
                         --enable-file-cons \
                         --enable-exo \
                         --enable-desktop-menu \
                         --enable-desktop-menu-dir-monitor \
                         --enable-panel-plugin")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("TODO", "README", "NEWS", "ChangeLog", "AUTHORS")
