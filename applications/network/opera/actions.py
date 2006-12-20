#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="opera-9.10-20061214.6-shared-qt.i386-en-521"

def install():
    shelltools.system("./install.sh DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/etc","config/opera6rc")
    pisitools.insinto("/usr/share/pixmaps","images/*.png")
