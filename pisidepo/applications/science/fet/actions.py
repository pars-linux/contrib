#!/usr/bin/python
#
#Ertugrul Erata ertugrulerata at gmail.com
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


def setup():
    shelltools.system("/usr/bin/qmake-qt4 fet.pro")

def build():
    autotools.make()


def install():
    pisitools.dobin("fet","/usr/share/fet")
    pisitools.dosym("/usr/share/fet/fet","/usr/bin/fet")
    pisitools.insinto("/usr/share/fet/translations","translations/*.qm")
    pisitools.insinto("/usr/share/fet/doc","doc/*")
    pisitools.doman("doc/fet.1")
    pisitools.remove("/usr/share/fet/doc/fet.1")
    pisitools.insinto("/usr/share/fet/sample_inputs","sample_inputs/*")