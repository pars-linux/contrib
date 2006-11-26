#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


def setup():
    shelltools.export("QTDIR","/usr/qt/3/")
    shelltools.system("/usr/qt/3/bin/qmake qtiplot")
    shelltools.system("/usr/qt/3/bin/qmake")

def build():
    autotools.make()


def install():
    autotools.install()