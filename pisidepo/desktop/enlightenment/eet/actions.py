#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Murat Şenel
#
#murattsenell@gmail.com

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="eet-0.9.10.027"

def setup():
    shelltools.system("cd /usr/bin && rm -rf eet eet_bench eet-config && cd /usr/include && rm -rf Eet.h && cd /usr/lib && rm -rf libeet.a libeet.la libeet.so libeet.so.0 libeet.so.0.9.10")
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("COPYING*", "README*", "NEWS")