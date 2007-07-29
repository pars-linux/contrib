#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools


WorkDir="PyQwt-%s" % get.srcVERSION()

def setup():
    shelltools.copytree("../PyQwt-%s" % get.srcVERSION(),"../PyQwt-%s-qt4" % get.srcVERSION())
    shelltools.cd("configure")
    shelltools.system("python configure.py -3 -I /usr/qt/3/include/qwt/")

    shelltools.cd("../../PyQwt-%s-qt4/configure" % get.srcVERSION())
    shelltools.system("python configure.py -I /usr/qt/4/include/qwt/")

def build():
    shelltools.cd("configure")
    autotools.make()

    shelltools.cd("../../PyQwt-%s-qt4/configure" % get.srcVERSION())
    autotools.make()



def install():
    shelltools.cd("configure")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pythonmodules.fixCompiledPy()

    shelltools.cd("../../PyQwt-%s-qt4/configure" % get.srcVERSION())
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pythonmodules.fixCompiledPy()
