#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Eren Türkay <turkay.eren@gmail.com>

WorkDir="LimeWire"

from pisi.actionsapi import pisitools

def setup():
    pass

def build():
    pass

def install():
    pisitools.insinto("/opt/limewire","*")