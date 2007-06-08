#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools


def setup():
    kde.configure("--with-external-geoip \
                   --with-external-tsocks")

def build():
    kde.make()

def install():
    kde.install()

    # remove files conflicts
    pisitools.removeDir("/usr/kde/3.5/share/icons/crystalsvg")

    # for using tsocks add  needed programs
    pisitools.dobin("src/tsocks/torkify")
