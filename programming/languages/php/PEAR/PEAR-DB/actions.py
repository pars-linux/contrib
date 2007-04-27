#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="DB-1.7.11"

def install():
    pisitools.insinto("/usr/share/php5/PEAR","DB.php")
    pisitools.insinto("/usr/share/php5/PEAR/DB","DB/*")
    pisitools.insinto("/usr/share/php5/PEAR/doc/DB","doc/*")
    pisitools.insinto("/usr/share/php5/PEAR/tests/DB","tests/*")
