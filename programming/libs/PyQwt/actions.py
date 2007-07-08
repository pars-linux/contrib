#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools


WorkDir="PyQwt-5.0.0"

def setup():
    shelltools.copytree("../PyQwt-5.0.0","../PyQwt-5.0.0-qt4")
    shelltools.cd("configure")
    shelltools.system("python configure.py -3 -I /usr/qt/3/include/qwt/")

    shelltools.cd("../../PyQwt-5.0.0-qt4/configure")
    shelltools.system("python configure.py -I /usr/qt/4/include/qwt/")

def build():
    shelltools.cd("configure")
    autotools.make()

    shelltools.cd("../../PyQwt-5.0.0-qt4/configure")
    autotools.make()



def install():
    shelltools.cd("configure")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pythonmodules.fixCompiledPy()

    shelltools.cd("../../PyQwt-5.0.0-qt4/configure")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pythonmodules.fixCompiledPy()