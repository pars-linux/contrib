#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Uğur Çetin <jnmbk@users.sourceforge.net>

from pisi.actionsapi import kde
from pisi.actionsapi import shelltools

def setup():
    shelltools.system("sed -i \"s:\$(LIB_KIO):-L${KDEDIR}/lib -lkio:\" kbfxconfigapp/Makefile.am && make -f Makefile.cvs")
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()