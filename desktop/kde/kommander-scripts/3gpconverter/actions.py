#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="3gpconverter-%s" % get.srcVERSION()

def install():
    pisitools.insinto("/usr/kde/3.5/bin", "3gpconverter-0.6.kmdr","3gpconverter.kmdr")
