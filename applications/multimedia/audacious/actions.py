#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "audacious-1.4.0-rc1"

def setup():
    autotools.configure("--enable-ipv6 \
                         --enable-chardet \
                         --enable-rpath \
                         --disable-gconf \
                         --enable-mcs \
                         --enable-xspf \
                         --disable-xmltest \
                         --enable-samplerate \
                         --enable-nls")
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("/usr/share/applications/audacious.desktop")
    pisitools.insinto("/usr/share/applications", "applications/audacious.desktop")

    pisitools.dodoc("ABOUT-NLS", "ChangeLog", "COPYING", "AUTHORS", "NEWS", "README")
