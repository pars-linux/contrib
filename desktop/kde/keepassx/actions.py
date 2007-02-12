#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


def setup():
    shelltools.system("/usr/bin/qmake-qt4 PREFIX=/{Install./usr/bin}")

def build():
    autotools.make()


def install():
    #autotools.install()
    pisitools.dobin("bin/keepass")
    pisitools.insinto("/usr/share/","share/*")
