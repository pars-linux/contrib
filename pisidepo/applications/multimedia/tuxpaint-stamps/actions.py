#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Murat Şenel <muratasenel@gmail.com>

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="tuxpaint-stamps-2006.10.15"

def setup():
    pisitools.dosed("Makefile","/usr/local","%s/usr" % get.installDIR())

def build():
    autotools.make()

def install():
    pisitools.dodir("/usr/share/tuxpaint")
    shelltools.system("make install-all")
    pisitools.dodoc("docs/*.txt")
