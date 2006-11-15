#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="MDB-1.3.0"

def install():
    pisitools.insinto("/usr/share/php5/PEAR", "MDB.php")
    pisitools.insinto("/usr/share/php5/PEAR/MDB", "MDB/*")
    pisitools.insinto("/usr/share/php5/PEAR/tests/MDB", "tests/*")
    docs = ['doc/*', 'MAINTAINERS', 'README', 'TODO']
    for doc in docs:
        pisitools.insinto("/usr/share/php5/PEAR/doc/MDB", doc)