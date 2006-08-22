#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Serkan Avcı <killer@wolke7.net>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def build():
    autotools.make("SOUND=1")

def install():
    pisitools.insinto("/usr/share/darkoberon", "*")
    pisitools.removeDir("/usr/share/darkoberon/src")
    pisitools.remove("/usr/share/darkoberon/Makefile")
    pisitools.remove("/usr/share/darkoberon/README")