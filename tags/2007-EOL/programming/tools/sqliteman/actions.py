#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    cmaketools.configure(installPrefix = "%s/usr" % get.installDIR())

def build():
    cmaketools.make()

def install():
    cmaketools.install()
    pisitools.domove("/usr/share/icons/sqliteman.png", "/usr/share/pixmaps/")
    pisitools.dodoc("AUTHORS", "README", "VERSION", "COPYING")
