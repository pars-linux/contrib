#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Uğur Çetin <jnmbk@users.sourceforge.net>

from pisi.actionsapi import autotools

WorkDir="subtitleeditor-0.11-alpha1"

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()
