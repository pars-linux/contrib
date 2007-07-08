#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

def setup():
    cmaketools.configure(installPrefix = "%s/%s" % (get.installDIR(), get.kdeDIR()))

def build():
    cmaketools.make()

def install():
    cmaketools.install()

