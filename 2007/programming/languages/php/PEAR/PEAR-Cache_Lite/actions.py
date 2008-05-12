#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="Cache_Lite-%s" % get.srcVERSION()

def install():
    pisitools.insinto("/usr/share/php5/PEAR/Cache", "Lite.php")
    pisitools.insinto("/usr/share/php5/PEAR/Cache/Lite", "Lite/*")
    pisitools.insinto("/usr/share/php5/PEAR/tests/Cache_Lite", "tests/*")
    items=['LICENSE','TODO','docs/*']
    for item in items:
        pisitools.insinto("/usr/share/php5/PEAR/doc/Cache_Lite", item)
