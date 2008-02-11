#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get

WorkDir = "smplayer-%s%s" % (get.srcVERSION().split("_", 1)[0],  get.srcVERSION().split("_", 1)[1])

def build():
    autotools.make("QMAKE=qmake-qt4 PREFIX=/usr")

def install():
    autotools.rawInstall("PREFIX=/usr DESTDIR=%s DOC_PATH=/usr/share/doc/%s" % (get.installDIR(),get.srcTAG()))
