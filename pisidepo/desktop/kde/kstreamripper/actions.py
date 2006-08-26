#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Uğur Çetin <jnmbk@users.sourceforge.net>

from pisi.actionsapi import scons
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("scons configure prefix=%s%s" % (get.installDIR(), get.kdeDIR()))

def build():
    scons.make()

def install():
    scons.install()
    pisitools.insinto("%s/share/icons/hicolor/32x32/apps" % get.kdeDIR(), "src/hi32-app-kstreamripper.png", "kstreamripper.png")
    pisitools.insinto("%s/share/icons/hicolor/16x16/apps" % get.kdeDIR(), "src/hi16-app-kstreamripper.png", "kstreamripper.png")