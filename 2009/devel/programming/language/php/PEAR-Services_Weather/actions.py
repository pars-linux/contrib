#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="Services_Weather-%s" % get.srcVERSION()

def install():
    pisitools.insinto("/usr/share/php5/PEAR/Services", "Weather*")
    pisitools.insinto("/usr/share/php5/PEAR/Services/images", "images/*")
    pisitools.insinto("/usr/share/php5/PEAR/Services", "buildMetarDB.php")
    pisitools.insinto("/usr/share/php5/PEAR/doc/Services_Weather", "examples/*")
