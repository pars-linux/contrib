#!/usr/bin/python
#
#Ertugrul Erata ertugrulerata at gmail.com
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import kde
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    shelltools.system("/usr/bin/qmake-qt4 fet.pro")

def build():
    kde.make()


def install():
    pisitools.dobin("fet","/usr/share/fet")
    pisitools.dosym("/usr/share/fet/fet","/usr/bin/fet")
    pisitools.insinto("/usr/share/fet/translations","translations/*.qm")
    pisitools.insinto("/usr/share/fet/doc","doc/*")
    pisitools.insinto("/usr/share/fet/sample_inputs","sample_inputs/*")