#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "devede-3.11"

def install():
    shelltools.system("sh install.sh prefix=/usr DESTDIR=%s" % get.installDIR())
