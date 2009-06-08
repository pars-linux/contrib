#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-bdb4 \
                         --disable-static \
                         --enable-reentrant \
                         --enable-dbus \
                         --enable-libnotify \
                         --enable-archive \
                         --disable-libxfce4mcs")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("NEWS", "README", "ChangeLog", "AUTHORS")
