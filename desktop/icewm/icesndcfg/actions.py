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
    pisitools.dosed("icesndcfg.pro", "/usr/local", "%s/usr" % get.installDIR())
    shelltools.system("echo >> icesndcfg.pro -e 'QMAKE_CXXFLAGS_RELEASE += %s'" % get.CXXFLAGS())
    shelltools.system("echo >> icesndcfg.pro -e 'QMAKE_CFLAGS_RELEASE += %s'" % get.CFLAGS())
#   addwrite ${QTDIR}/etc/settings   
    shelltools.system("lrelease icesndcfg.pro") 
    shelltools.system("qmake")

def build():
    autotools.make()
    shelltools.system("strip -s icesndcfg")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/share/icesndcfg/locale", "icesndcfg_ua.qm")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "INSTALL")
