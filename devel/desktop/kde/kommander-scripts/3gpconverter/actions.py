#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="3gpconverter-%s" % get.srcVERSION()

def install():
    pisitools.insinto("/usr/kde/3.5/bin", "3gpconverter-0.6.kmdr","3gpconverter.kmdr")

    pisitools.dodoc("changelog", "readme")
