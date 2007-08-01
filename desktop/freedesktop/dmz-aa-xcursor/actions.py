#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "."

def install():
    pisitools.dodir("/usr/share/cursors/xorg-x11/DMZ-AA/")
    shelltools.copytree("Vanilla-DMZ-AA/cursors/","%s/usr/share/cursors/xorg-x11/DMZ-AA/cursors" % get.installDIR(), True)
