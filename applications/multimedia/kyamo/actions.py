#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools

WorkDir="kyamo-0.40a4-2"

def setup():
    kde.configure()

def build():
    kde.make()

def install():
    kde.install() 
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "INSTALL", "README")
