#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Erhan Onur Şendağ <onursendag@yahoo.com>

from pisi.actionsapi import autotools


def setup():
    autotools.configure()
    
def build():
    autotools.make()

def install():
    autotools.install()