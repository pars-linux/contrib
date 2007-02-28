#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="qwt-5.0.1"

def setup():
    shelltools.copytree("../qwt-5.0.1","../qwt-5.0.1-qt4")
    shelltools.system("qmake qwt.pro")
    shelltools.cd("../qwt-5.0.1-qt4")
    shelltools.system("qmake-qt4 qwt.pro")

def build():
    autotools.make()
    shelltools.cd("../qwt-5.0.1-qt4")
    autotools.make()


def install():
    pisitools.insinto("%s/lib/" % get.qtDIR(),"lib/*")
    pisitools.insinto("%s/include/qwt" % get.qtDIR() ,"src/*.h")

    pisitools.insinto("/usr/share/doc/%s" % get.srcTAG(), "examples")
    pisitools.insinto("/usr/share/doc/%s" % get.srcTAG(), "doc/html")
    pisitools.doman("doc/man/man3/*.3")

    pisitools.insinto("%s/plugins/designer" % get.qtDIR(),"designer/plugins/designer/*.so")

    shelltools.cd("../qwt-5.0.1-qt4")
    pisitools.insinto("/usr/qt/4/lib/","lib/*")
    pisitools.insinto("/usr/qt/4/include/qwt","src/*.h")

    pisitools.insinto("/usr/qt/4/plugins/designer","designer/plugins/designer/*.so")