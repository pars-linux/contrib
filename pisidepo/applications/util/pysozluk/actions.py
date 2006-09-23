#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Murat Şenel <muratasenel@gmail.com>

from pisi.actionsapi import pisitools

WorkDir="PySozluk-1.0.2"

def setup():
    pass

def build():
    pass

def install():
    pisitools.dobin("pysozluk")
    pisitools.insinto("/usr/share/pysozluk/bayrak", "bayrak/*")
    pisitools.insinto("/usr/share/pysozluk", "pysozluk_konsole.py")
    pisitools.insinto("/usr/share/pysozluk/yardim", "yardim/*")
    pisitools.insinto("/usr/share/pysozluk", "pysozluk.py")
    pisitools.insinto("/usr/share/applications", "pysozluk.desktop")
    pisitools.insinto("/usr/share/pixmaps", "pysozluk.png")
    pisitools.dodoc("README")

