#!/usr/bin/python
# -*- coding: utf-8 -*-
#Murat Şenel <> muratasenel@gmail.com <>

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = ""

def install():
    pisitools.dodir("/opt/bioclipse")
    shelltools.system("unzip bioclipse-1.0.linux.gtk.x86.zip")
    shelltools.cd("bioclipse")
    pisitools.insinto("/opt/bioclipse", "*")


