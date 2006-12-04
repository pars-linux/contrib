#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="MDB2-2.3.0"

def install():
    pisitools.insinto("/usr/share/php5/PEAR", "MDB2")
    pisitools.insinto("/usr/share/php5/PEAR/MDB2", "MDB2/*")
    pisitools.insinto("/usr/share/php5/PEAR/doc/MDB2", "docs/*")
    pisitools.insinto("/usr/share/php5/PEAR/tests/MDB2", "tests/*")