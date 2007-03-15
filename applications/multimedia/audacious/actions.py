#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

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

    pisitools.dodoc("ABOUT-NLS", "ChangeLog", "COPYING", "AUTHORS", "INSTALL", "NEWS", "README")