#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Murat Şenel
#
#muratasenel@gmail.com

from pisi.actionsapi import kde

WorkDir = "ksimus-floatingpoint-0.3.6"

def setup():
    kde.configure()

def build():
    kde.make()


def install():
    kde.install()