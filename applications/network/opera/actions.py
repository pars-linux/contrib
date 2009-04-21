#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="opera-9.52-2091.gcc3-shared-qt3.i386"

def install():
    shelltools.system("./install.sh DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/etc","etc/opera6rc")

    pisitools.insinto("/usr/share/pixmaps", "usr/share/pixmaps/opera.xpm")

    for size in ["16x16","22x22","32x32","48x48"]:
      pisitools.insinto("/usr/share/icons/hicolor/%s/apps" % size, "usr/share/icons/hicolor/%s/apps/opera.png" % size)
