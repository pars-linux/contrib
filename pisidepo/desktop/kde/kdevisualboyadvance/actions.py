#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Uğur Çetin <jnmbk@users.sourceforge.net>

from pisi.actionsapi import kde

WorkDir="KDEVisualBoyAdvance-0.3(beta)"

def setup():
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()
