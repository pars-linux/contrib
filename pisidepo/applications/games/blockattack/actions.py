#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Uğur Çetin <jnmbk@users.sourceforge.net>

from pisi.actionsapi import scons
from pisi.actionsapi import get

def setup():
    pass

def build():
    pass

def install():
    scons.make("install blockattack destdir=%s prefix=/usr" % get.installDIR())