#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="freefont-%s" % get.srcVERSION()

def install():
    pisitools.dodoc("AUTHORS","ChangeLog","README","COPYING")
    pisitools.insinto("/usr/share/fonts/default/TrueType/","*.ttf")
