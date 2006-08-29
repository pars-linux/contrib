#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Eren Türkay <turkay.eren@gmail.com>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    pass
def build():
    autotools.make()

def install():
    pisitools.dobin("ctronome")
    pisitools.insinto("/usr/share/ctronome","*.wav")