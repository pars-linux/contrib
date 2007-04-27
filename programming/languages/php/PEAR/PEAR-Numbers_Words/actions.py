#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="Numbers_Words-0.15.0"

def install():
    pisitools.insinto("/usr/share/php5/PEAR/Numbers", "Words*")
    pisitools.insinto("/usr/share/php5/PEAR/doc/Numbers_Words", "README")
    pisitools.insinto("/usr/share/php5/PEAR/tests/Numbers_Words", "tests/*")