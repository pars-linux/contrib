#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# turkay.eren@gmail.com
#######################

from pisi.actionsapi import autotools

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()