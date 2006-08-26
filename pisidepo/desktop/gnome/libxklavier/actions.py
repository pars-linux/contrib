#!/usr/bin/python
#
#Ertugrul Erata ertugrulerata at gmail.com
#

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools


def setup():
    autotools.configure("--enable-xkb-support --enable-xmm-support --enable-doxygen")

def build():
    autotools.make()


def install():
    autotools.install()