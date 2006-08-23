#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Eren Türkay <turkay.eren@gmail.com>

from pisi.actionsapi import perlmodules

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()
    perlmodules.make("test")

def install():
    perlmodules.install()