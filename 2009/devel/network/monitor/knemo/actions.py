#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DCMAKE_BUILD_TYPE=release -DCMAKE_INSTALL_PREFIX=%s" % get.kdeDIR())

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
