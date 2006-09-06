#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Murat Şenel
#
#muratasenel@gmail.com

from pisi.actionsapi import kde

WorkDir = "dekorator-0.3"

def setup():
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()