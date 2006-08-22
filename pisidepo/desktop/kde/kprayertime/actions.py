#
#Pardox pardox2006 at hotmail dot com
#

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "kprayertime-0.9.9.4"

def setup():
#   make -f Makefile.cvs && ./configure --prefix=/usr/kde/3.5 && make && make install
    shelltools.system("make -f Makefile.cvs")
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()
