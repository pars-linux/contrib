#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="HTML_Table_Matrix-1.0.9"

def install():
    pisitools.insinto("/usr/share/php5/PEAR/HTML/Table", "Matrix*")
    pisitools.insinto("/usr/share/php5/PEAR/doc/HTML_Table_Matrix", "examples/*")