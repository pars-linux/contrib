#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Murat Şenel <muratasenel@gmail.com>

from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules

WorkDir="Twisted-2.4.0"

def install():
    shelltools.cd("TwistedCore-2.4.0")
    pythonmodules.install()