#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "%s_%s" % (get.srcNAME(), get.srcVERSION())

def install():
    pisitools.insinto("/opt/phex", "*")
