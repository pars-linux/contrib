#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="Date-1.4.7"

def install():
    pisitools.insinto("/usr/share/php5/PEAR", "Date*")
    pisitools.insinto("/usr/share/php5/PEAR/doc/Date", "docs/*")
    pisitools.insinto("/usr/share/php5/PEAR/tests/Date", "tests/*")