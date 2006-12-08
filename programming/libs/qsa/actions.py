#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="qsa-x11-free-1.1.4"



def define_global():
    shelltools.export("QSA_BUILD_PREFIX", "%s/lib" % get.workDIR())


def setup():
    define_global()
    shelltools.system("qmake qsa.pro")
    shelltools.system("qmake")
    autotools.rawConfigure()

def build():
    define_global()
    autotools.make()


def install():
    pisitools.insinto("/usr/qt/3/include","src/qsa/*.h")
    pisitools.insinto("/usr/qt/3/include","src/ide/qsworkbench.h")
    pisitools.insinto("/usr/qt/3/lib","lib/libqsa.so*")
    pisitools.insinto("/usr/qt/3/plugins/designer","plugins/designer/libqseditorplugin.so")
    pisitools.insinto("/usr/share/doc/%s" % get.srcTAG(), "examples")