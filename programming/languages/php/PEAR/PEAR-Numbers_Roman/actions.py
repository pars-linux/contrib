#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="Numbers_Roman-1.0.1"

def install():
    pisitools.insinto("/usr/share/php5/PEAR/Numbers", "Roman.php")
    pisitools.insinto("/usr/share/php5/PEAR/doc/Numbers_Roman", "docs/*")