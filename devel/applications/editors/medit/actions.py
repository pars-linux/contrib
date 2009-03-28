#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.rawConfigure()

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("README" , "COPYING" , "NEWS" , "AUTHORS" , "LICENSE")
    pisitools.remove("/usr/share/icons/hicolor/icon-theme.cache")
    pisitools.remove("/usr/share/icons/hicolor/48x48/apps/medit.png")
    pisitools.removeDir("/usr/lib/python2.5/")