#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="DB_DataObject-1.8.5"

def install():
    pisitools.insinto("/usr/share/php5/PEAR/DB", "DataObject*")
    pisitools.insinto("/usr/share/php5/PEAR/doc/DB_DataObject", "docs/*")