#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Eren Türkay <turkay.eren@gmail.com>

from pisi.actionsapi import perlmodules

WorkDir="Audio-1.029"

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

def install():
    perlmodules.install()