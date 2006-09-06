#!/usr/bin/python
# -*- coding: utf-8 -*-
#Murat Şenel <> muratasenel@gmail.com <>

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = ""

def install():

    pisitools.dodir("/opt/bioclipse")
    shelltools.system("unzip bioclipse-0.9.2.linux.gtk.x86.zip")
    shelltools.cd("bioclipse")
    pisitools.insinto("/opt/bioclipse", "*")


