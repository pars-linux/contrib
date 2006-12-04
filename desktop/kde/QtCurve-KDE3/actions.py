#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

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