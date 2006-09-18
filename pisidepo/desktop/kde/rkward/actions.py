#!/usr/bin/python
#
#Ertugrul Erata ertugrulerata at gmail.com
#

from pisi.actionsapi import get
from pisi.actionsapi import kde
from pisi.actionsapi import pisitools

def setup():
    kde.configure("--with-r-home=/usr/lib/R \
                   --with-r-includes=/usr/lib/R/include")

def build():
    kde.make()

def install():
    kde.install()
    #TODO: this one seems better than the one in kdelibs
    pisitools.remove("%s/share/apps/katepart/syntax/r.xml" % get.kdeDIR())
    #fix conflict with R
    pisitools.remove("/usr/lib/R/library/R.css")
