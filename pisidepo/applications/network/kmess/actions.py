#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Uğur Çetin <jnmbk@users.sourceforge.net>

from pisi.actionsapi import kde

WorkDir="kmess-1.5pre1"

def setup():
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()
