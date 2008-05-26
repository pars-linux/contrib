#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

WorkDir="elementtree-1.2.7-20070827-preview"

def install():
    pythonmodules.install()

    pisitools.dohtml("docs/")
    pisitools.dodoc("CHANGES", "README")
