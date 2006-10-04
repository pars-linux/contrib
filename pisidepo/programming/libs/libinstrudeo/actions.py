#!/usr/bin/python
#
#Ertugrul Erata ertugrulerata at gmail.com
#

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools


def setup():
    shelltools.export("libxmlpp_CFLAGS","-I/usr/include/libxml++-1.0 -I/usr/lib/libxml++-1.0/include")
    shelltools.export("libxmlpp_LIBS","-L/usr/lib -lxml++-1.0")
    autotools.configure()

def build():
    autotools.make()


def install():
    autotools.install()