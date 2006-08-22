#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Eren Türkay <turkay.eren@gmail.com>

from pisi.actionsapi import kde
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools

def setup():
    kde.configure()

def build():
    shelltools.system("autoheader")
    autotools.autoconf()
    kde.make()

def install():
    kde.install()