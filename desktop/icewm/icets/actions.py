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
#   sed -e "s:/usr/local:/usr:" -i ${PN}.pro || die "sed failed"
#   sed -e 's:/usr/local:/usr:g' -i ${PN}.cpp || die "sed failed"
    
    pisitools.dosed("icets.pro", "/usr/local", "%s/usr" % get.installDIR())
    pisitools.dosed("icets.cpp", "/usr/local", "%s/usr" % get.installDIR())
    
    shelltools.system("echo >> icets.pro -e 'QMAKE_CXXFLAGS_RELEASE += %s'" % get.CXXFLAGS())
    shelltools.system("echo >> icets.pro -e 'QMAKE_CFLAGS_RELEASE += %s'" % get.CFLAGS())
    shelltools.system("lrelease icets.pro")
    shelltools.system("qmake")

def build():
    autotools.make()
    shelltools.system("strip -s icets")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/share/icets/locale", "icets_ua.qm")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "INSTALL", "README", "TODO")
