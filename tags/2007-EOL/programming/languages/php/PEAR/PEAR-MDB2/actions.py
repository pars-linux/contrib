#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="MDB2-%s" % get.srcVERSION()

def install():
    pisitools.insinto("/usr/share/php5/PEAR", "MDB2.php")
    pisitools.insinto("/usr/share/php5/PEAR/MDB2", "MDB2/*")
    pisitools.insinto("/usr/share/php5/PEAR/doc/MDB2", "docs/*")
    pisitools.insinto("/usr/share/php5/PEAR/tests/MDB2", "tests/*")