#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools

def setup():
    kde.configure("--enable-alsa \
                         --enable-oss \
                         --enable-arts \
                         --enable-jack")

def build():
    kde.make()

def install():
    kde.install()
    
    pisitools.dodoc("ChangeLog", "AUTHORS")
