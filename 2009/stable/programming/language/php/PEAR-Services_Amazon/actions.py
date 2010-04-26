#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="Services_Amazon-%s" % get.srcVERSION()

def install():
    pisitools.insinto("/usr/share/php5/PEAR/Services", "Amazon*")
    pisitools.insinto("/usr/share/php5/PEAR/doc/Services_Amazon", "examples/*")
