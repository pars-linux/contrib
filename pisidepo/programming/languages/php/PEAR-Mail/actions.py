#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="Mail-1.1.14"

def install():
    pisitools.insinto("/usr/share/php5/PEAR", "Mail.php")
    pisitools.insinto("/usr/share/php5/PEAR/Mail", "Mail/*")
    pisitools.insinto("/usr/share/php5/PEAR/tests/Mail", "tests/*")