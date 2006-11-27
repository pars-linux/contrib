#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    shelltools.system("qmake qtiplot")
    shelltools.system("/usr/qt/3/bin/qmake")

def build():
    autotools.make()


def install():
    pisitools.dobin("qtiplot/qtiplot","/usr/share/qtiplot")
    pisitools.dosym("/usr/share/qtiplot/qtiplot","/usr/bin/qtiplot")
    pisitools.insinto("/usr/share/qtiplot/translations","qtiplot/translations/qtiplot_*.ts")
    pisitools.insinto("/usr/share/qtiplot", "manual/docbook-en")
    pisitools.insinto("/usr/share/sip/qti", "qtiplot/src/qti.sip")