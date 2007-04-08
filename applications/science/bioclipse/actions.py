#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def install():
    pisitools.dodir("/opt/bioclipse")
    shelltools.cd("bioclipse")
    pisitools.insinto("/opt/bioclipse", "*")


