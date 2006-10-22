#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Eren Türkay <turkay.eren@gmail.com>

from pisi.actionsapi import kde
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()
    # change permissions of *.qtcurve files to use
    shelltools.chmod("%s/%s/share/apps/qtcurve" % (get.installDIR(),get.kdeDIR()), 0777)
    shelltools.chmod("%s/%s/share/apps/qtcurve/*" % (get.installDIR(),get.kdeDIR()), 0777)