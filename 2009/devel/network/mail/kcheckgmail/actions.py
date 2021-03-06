#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    cmaketools.configure(installPrefix=get.kdeDIR(), sourceDir=".")

def build():
    cmaketools.make()

def install():
    cmaketools.install("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "README", "TODO")
