#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get



def setup():
    autotools.configure("--with-ssl --with-qt-dir=%s" % get.qtDIR())

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("README", "README.FREEBSD", "README.GPG", "README.ICS", "README.OPENSSL", "LICENSE", "INSTALL", "ChangeLog", "doc/*")

#
    shelltools.cd("plugins/rms")
    autotools.configure()
    autotools.make()
    autotools.install()
    shelltools.cd("../../")
 
#
    shelltools.cd("plugins/qt-gui")
    autotools.configure("--with-kde")
    autotools.make()
    autotools.install()
    shelltools.cd("../../")
 
# 
    shelltools.cd("plugins/msn")
    autotools.configure()
    autotools.make()
    autotools.install()
    shelltools.cd("../../")

#    
    shelltools.cd("plugins/osd")
    shelltools.system("./build")
    autotools.configure("--prefix=/usr")
    autotools.make()
    autotools.install()
    shelltools.cd("../../")

#
    shelltools.cd("plugins/console")
    autotools.configure()
    autotools.make()
    autotools.install()
    shelltools.cd("../../")

#
    shelltools.cd("plugins/auto-reply")
    autotools.configure()
    autotools.make()
    autotools.install()
    shelltools.cd("../../")

#    
    shelltools.cd("plugins/email")
    autotools.configure()
    autotools.make()
    autotools.install()
    shelltools.cd("../../")