#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="ipt-qt-conf-1.3.2/ipt-qt-conf"

def setup():
    shelltools.system("qmake")

def build():
    autotools.make()


def install():
    pisitools.dobin("ipt-qt-conf","/usr/share/ipt-qt-conf")

    pisitools.dosym("/usr/share/ipt-qt-conf/ipt-qt-conf","/usr/bin/ipt-qt-conf")

    pisitools.insinto("/usr/share/ipt-qt-conf/examples","examples/*")
    pisitools.insinto("/usr/share/ipt-qt-conf/","*.*")
