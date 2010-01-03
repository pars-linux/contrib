#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

WorkDir='moodin'

def setup():
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()

    pisitools.dodoc("COPYING", "AUTHORS")
