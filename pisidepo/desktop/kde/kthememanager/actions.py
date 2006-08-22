#!/usr/bin/python
#-*- coding: UTF-8 -*- 
#
# turkay.eren@gmail.com
#######################

from pisi.actionsapi import kde

def setup():
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()