#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Eren Türkay <turkay.eren@gmail.com>

from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir="pouetchess_src_0.2.0"

def setup():
    shelltools.system("/usr/bin/scons configure prefix=/usr datadir=/usr/share/pouetchess")

def build():
    shelltools.system("/usr/bin/scons")

def install():
    shelltools.system("/usr/bin/scons install")

    shelltools.system("rm /usr/bin/.sconsign")
    shelltools.system("find /usr/share/pouetchess/ -name .sconsign -exec rm {} \;")
    pisitools.dodir("/usr/bin")
    pisitools.dodir("/usr/share")
    shelltools.move("/usr/bin/pouetChess", "%s/usr/bin/" % get.installDIR())
    shelltools.move("/usr/share/pouetchess", "%s/usr/share/pouetchess" % get.installDIR())