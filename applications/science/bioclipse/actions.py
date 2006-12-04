#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def install():
    pisitools.dodir("/opt/bioclipse")
    shelltools.system("unzip bioclipse-1.0.linux.gtk.x86.zip")
    shelltools.cd("bioclipse")
    pisitools.insinto("/opt/bioclipse", "*")


