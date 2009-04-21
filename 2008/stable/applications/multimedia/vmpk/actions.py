#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    cmaketools.configure()
    shelltools.cd("translations")
    shelltools.system("lrelease-qt4 *.ts")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto ("/usr/share/locale", "translations/*.qm")
    pisitools.dosym ("/usr/share/pixmaps/vmpk_48x48.png", "/usr/share/pixmaps/vmpk.png")
    pisitools.removeDir("/usr/share/doc/packages/")

    pisitools.dodoc("NEWS", "README", "AUTHORS", "ChangeLog", "COPYING", "TODO")
