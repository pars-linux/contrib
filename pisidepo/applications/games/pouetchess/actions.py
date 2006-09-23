#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Eren Türkay <turkay.eren@gmail.com>

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import scons

WorkDir="pouetchess_src_0.2.0"

def setup():
    shelltools.system("scons configure prefix=/usr datadir=/usr/share/pouetchess")

def build():
    scons.make()

def install():
    pisitools.dobin("bin/pouetChess")
    pisitools.insinto("/usr/share/pouetchess", "data/*")