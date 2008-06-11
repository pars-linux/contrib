#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-shm \
                         --enable-spell=gtkspell")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/pixmaps/", "xchat.png")
    pisitools.insinto("/usr/share/applications/", "xchat.desktop")

    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "HACKING", "README")
