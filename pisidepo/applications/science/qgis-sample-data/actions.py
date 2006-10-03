#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Murat Şenel <muratasenel@gmail.com>

from pisi.actionsapi import pisitools

WorkDir="qgis_sample_data"

def setup():
    pass

def build():
    pass

def install():
    pisitools.dodir("/usr/share/qgis/sample")
    pisitools.insinto("/usr/share/qgis/sample", "*")
