#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="qwt-5.0.0"

def setup():
    shelltools.system("qmake qwt.pro")

    shelltools.cd("designer")
    shelltools.system("qmake designer.pro")

def build():
    autotools.make()

    shelltools.cd("designer")
    autotools.make()

def install():
    pisitools.insinto("/usr/lib/","lib/*")
    pisitools.insinto("/usr/include/qwt","include/*")
    pisitools.insinto("/usr/share/doc/%s" % get.srcTAG(), "examples")
    pisitools.insinto("/usr/share/doc/%s" % get.srcTAG(), "doc/html")
    pisitools.insinto("%s/plugins/designer" % get.qtDIR(),"designer/plugins/designer/*.so")
