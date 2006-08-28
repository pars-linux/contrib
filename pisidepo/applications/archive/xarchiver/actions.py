#!/usr/bin/python
#
#Ertugrul Erata ertugrulerata at gmail.com
#

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir="Xarchiver-0.3.3"

def setup():
    autotools.configure()

def build():
    autotools.make()


def install():
    autotools.install()
    pisitools.removeDir("/usr/share/locale")
    pisitools.domo("po/tr.po","tr","xarchiver.mo")