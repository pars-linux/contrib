#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Eren Türkay <turkay.eren@gmail.com>

from pisi.actionsapi import perlmodules
from pisi.actionsapi import shelltools

def setup():
    perlmodules.configure()

def build():
    perlmodules.make("test")
    perlmodules.make()

def install():
    perlmodules.install()