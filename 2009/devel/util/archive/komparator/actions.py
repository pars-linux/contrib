#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

# sormadan paketin ismini değiştirmek istemedim, komparator4 olacak sonra
WorkDir = "komparator4-0.1b"

def setup():
    cmaketools.configure("-DCMAKE_BUILD_TYPE=release", installPrefix="/usr/kde/4")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README", "TODO")
