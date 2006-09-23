#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Uğur Çetin <jnmbk@users.sourceforge.net>

from pisi.actionsapi import kde

WorkDir = "kbfx-0.4.9.2rc2"

def setup():
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()