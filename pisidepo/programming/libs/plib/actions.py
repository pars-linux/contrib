#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Uğur Çetin <jnmbk@users.sourceforge.net>

from pisi.actionsapi import autotools

def setup():
    autotools.configure()

def build():
    pass

def install():
    autotools.install()