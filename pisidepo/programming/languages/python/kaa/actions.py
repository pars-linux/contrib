#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Murat Şenel <muratasenel@gmail.com>

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

def install():
    pythonmodules.install()
    pisitools.remove("/usr/bin/mminfo")
