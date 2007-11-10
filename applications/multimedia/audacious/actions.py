#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

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

    # We need this workaround since Default skin is buggy.
    pisitools.removeDir("/usr/share/audacious/Skins/Default")
    pisitools.rename("/usr/share/audacious/Skins/Refugee", "Default")

    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "doc/libaudacious/*.txt")
