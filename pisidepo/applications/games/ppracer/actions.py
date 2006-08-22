#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Eren Türkay <turkay.eren@gmail.com>

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir="ppracer-0.5alpha"

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()
    shelltools.system("/usr/bin/mv /usr/share/ppracer %s/usr/share/" % get.installDIR())
    pisitools.insinto("/usr/share/ppracer/translations", "data/translations/tr_TR.nut")