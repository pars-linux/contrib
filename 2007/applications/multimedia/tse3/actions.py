#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-mutex \
                         --with-oss \
                         --with-alsa \
                         --with-aRts")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("THANKS", "TODO", "NEWS", "AUTHORS", "ChangeLog")
    pisitools.domove("/usr/doc/tse3-0.3.1/", "/usr/share/doc/%s/html/" % get.srcTAG())
    pisitools.removeDir("/usr/doc")
