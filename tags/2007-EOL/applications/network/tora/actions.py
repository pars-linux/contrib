#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--prefix=/usr \
                         --with-kde \
                         --with-qt-dir=/usr/qt/3 \
                         --with-qscintilla-includes=/usr/qt/3/include")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("LICENSE.txt", "BUGS", "NEWS", "README", "TODO")
