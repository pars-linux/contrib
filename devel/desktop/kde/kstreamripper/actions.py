#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import scons
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("scons configure prefix=%s%s" % (get.installDIR(), get.kdeDIR()))

def build():
    scons.make()

def install():
    shelltools.export("PATH", "%s/bin:%s" % (get.kdeDIR(), get.ENV("PATH")))
    scons.install()
    pisitools.insinto("%s/share/icons/hicolor/32x32/apps" % get.kdeDIR(), "src/hi32-app-kstreamripper.png", "kstreamripper.png")
    pisitools.insinto("%s/share/icons/hicolor/16x16/apps" % get.kdeDIR(), "src/hi16-app-kstreamripper.png", "kstreamripper.png")

