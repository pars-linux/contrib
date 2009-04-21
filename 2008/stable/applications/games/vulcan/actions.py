#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def setup():
    pisitools.dosed("Makefile", "pardusCC", get.CC())
    pisitools.dosed("Makefile", "pardusLD", get.CC())
    pisitools.dosed("Makefile", "pardusCFLAGS", get.CFLAGS())

def build():
    autotools.make("-j1 \
                    PREFIX=/usr")

def install():
    autotools.rawInstall('DESTDIR="%s" PREFIX=/usr' % get.installDIR())

    pisitools.dodoc("ChangeLog", "COPYING", "IDEAS", "README", "TECH")

