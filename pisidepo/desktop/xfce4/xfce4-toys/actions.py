#!/usr/bin/python
#
#Ertugrul Erata ertugrulerata at gmail.com
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    autotools.configure()

def build():
    autotools.make()


def install():
    autotools.install()
    pisitools.domo("po/tr.po","tr","xfce4-toys.mo")