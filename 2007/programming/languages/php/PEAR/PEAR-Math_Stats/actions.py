#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="Math_Stats-0.9.0beta3"

def install():
    pisitools.insinto("/usr/share/php5/PEAR/Math", "Stats.php")
    pisitools.insinto("/usr/share/php5/PEAR/doc/Math_Stats", "examples/*")
    pisitools.insinto("/usr/share/php5/PEAR/tests/Math_Stats", "test/*")