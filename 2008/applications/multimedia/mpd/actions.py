#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    autotools.configure("--disable-static \
                         --enable-pulse \
                         --enable-ao")

def build():
    autotools.make()

def install():
    autotools.install()

    # remove built-in files and add these to valid directory
    pisitools.removeDir("/usr/share/doc/mpd")
    pisitools.dodoc("AUTHORS", "README", "COMMANDS", "TODO")
