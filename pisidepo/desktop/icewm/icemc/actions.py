#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.


from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    pisitools.dosed("icemc.pro", "/usr/local", "%s/usr" % get.installDIR())
#   shelltools.system('echo >> icemc.pro -e "QMAKE_CXXFLAGS_RELEASE += "%s"\nQMAKE_CFLAGS_RELEASE += "%s""' % (get.CXXFLAGS(), get.CFLAGS()))
    shelltools.system("echo >> icemc.pro -e 'QMAKE_CXXFLAGS_RELEASE += %s'" % get.CXXFLAGS())
    shelltools.system("echo >> icemc.pro -e 'QMAKE_CFLAGS_RELEASE += %s'" % get.CFLAGS())
#   addwrite ${QTDIR}/etc/settings
    shelltools.system("lrelease icemc.pro")
    shelltools.system("qmake")

def build():
    autotools.make()
    shelltools.system("strip -s icemc")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/share/icemc/locale", "icemc_ua.qm")
    pisitools.insinto("/usr/share/icemc", "*.xpm")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "INSTALL") 