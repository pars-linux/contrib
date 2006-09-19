#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Uğur Çetin <jnmbk@users.sourceforge.net>

from pisi.actionsapi import pisitools

WorkDir="openttd-0.4.8-RC1-scenarios"

def setup():
    pass

def build():
    pass

def install():
    pisitools.insinto("/usr/share/openttd/scenario", "*")
