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