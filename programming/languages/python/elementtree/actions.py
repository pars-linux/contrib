#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Murat Şenel <muratasenel@gmail.com>

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

WorkDir="elementtree-1.2.6-20050316"

def install():
    pythonmodules.install()
    pisitools.dodoc("PKG-INFO", "CHANGES", "README")
    pisitools.dohtml("docs/")
