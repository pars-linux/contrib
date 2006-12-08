#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="Console_Table-1.0.5"

def install():
    pisitools.insinto("/usr/share/php5/PEAR/Console", "Table.php")
    pisitools.insinto("/usr/share/php5/PEAR/tests/Console_Table", "tests/*")