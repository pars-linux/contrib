#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Murat Şenel <muratasenel@gmail.com>

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def install():
    pisitools.dodir("/etc/freevo")
    pisitools.dodir("/var/cache/freevo")
    pisitools.dodir("/var/log/freevo")
    pythonmodules.install()
    pisitools.insinto("/etc/freevo", "ui/doc/local_conf.py.example")
    pisitools.rename("/etc/freevo/local_conf.py.example", "local_conf.py")
