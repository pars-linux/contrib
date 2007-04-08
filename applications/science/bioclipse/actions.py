#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

WorkDir="bioclipse"

def install():
    pisitools.dodir("/opt/bioclipse")
    pisitools.insinto("/opt/bioclipse", "*")


