#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="Net_SmartIRC-%s"  % get.srcVERSION()

def install():
    pisitools.insinto("/usr/share/php5/PEAR/Net", "SmartIRC*")
    pisitools.insinto("/usr/share/php5/PEAR/doc/Net_SmartIRC", "docs/*")
    pisitools.insinto("/usr/share/php5/PEAR/doc/Net_SmartIRC/examples", "examples/*")
