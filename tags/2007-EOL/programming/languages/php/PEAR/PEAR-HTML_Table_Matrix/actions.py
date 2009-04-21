#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="HTML_Table_Matrix-%s" % get.srcVERSION()

def install():
    pisitools.insinto("/usr/share/php5/PEAR/HTML/Table", "Matrix*")
    pisitools.insinto("/usr/share/php5/PEAR/doc/HTML_Table_Matrix", "examples/*")
