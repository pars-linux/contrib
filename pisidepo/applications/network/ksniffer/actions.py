#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# turkay.eren@gmail.com
#######################

from pisi.actionsapi import kde

WorkDir="ksniffer-0.2-alpha1"

def setup():
    kde.configure()

def build():
    kde.make()

def install():
    kde.install() 
