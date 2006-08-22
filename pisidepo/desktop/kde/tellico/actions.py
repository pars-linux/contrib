#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Eren Türkay <turkay.eren@gmail.com>

from pisi.actionsapi import kde

def setup():
    kde.configure("--enable-libkcddb --enable-libkcal")

def build():
    kde.make()

def install():
    kde.install()