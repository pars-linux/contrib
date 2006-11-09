#!/usr/bin/python
#
#Ertugrul Erata ertugrulerata at gmail.com
#

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir="xarchiver-0.4.2rc2"

def setup():
    autotools.configure()

def build():
    autotools.make()


def install():
    autotools.install()
    pisitools.domo("po/tr.po","tr","xarchiver.mo")