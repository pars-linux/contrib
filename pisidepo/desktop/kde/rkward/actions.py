#!/usr/bin/python
#
#Ertugrul Erata ertugrulerata at gmail.com
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import kde


def setup():
    kde.configure("--with-r-home=/usr/lib/R --with-r-includes=/usr/lib/R/include")

def build():
    kde.make()


def install():
    kde.install()
    pisitools.remove("/usr/kde/3.5/share/apps/katepart/syntax/r.xml")