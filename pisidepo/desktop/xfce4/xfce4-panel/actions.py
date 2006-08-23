#!/usr/bin/python
#
#Ertugrul Erata ertugrulerata at gmail.com
#

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools


def setup():
    autotools.configure()

def build():
    autotools.make()


def install():
    autotools.install()
    pisitools.removeDir("/usr/share/locale")
    pisitools.removeDir("/usr/share/xfce4/doc/fr")
    pisitools.removeDir("/usr/share/xfce4/doc/he")
    pisitools.domo("po/tr.po","tr","xfce4-panel.mo")