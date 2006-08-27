#!/usr/bin/python
#-*- coding: UTF-8 -*-
#
# Uğur Çetin
# jnmbk@users.sourceforge.net

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools


def setup():
    autotools.configure()

def build():
    shelltools.system("cp /usr/include/lcms/* .")
    autotools.make()

def install():
    autotools.install()