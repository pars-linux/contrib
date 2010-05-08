#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--prefix=/usr \
                         --with-jack \
                         --with-alsa")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/share/milkytracker", "resources")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "docs/*.rtf", "docs/readme_rtaudio", "docs/readme_unix", "docs/TiTAN.nfo")
    pisitools.dohtml("docs/*.html")
