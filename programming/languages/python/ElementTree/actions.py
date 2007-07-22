#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

WorkDir="elementtree-1.2.6-20050316"

def install():
    pythonmodules.install()


    pisitools.dohtml("docs/")
    pisitools.dodoc("CHANGES", "README")
