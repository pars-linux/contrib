#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="Net_Sieve-1.2.0b1"

def install():
    pisitools.insinto("/usr/share/php5/PEAR/Net", "Sieve.php")
    pisitools.insinto("/usr/share/php5/PEAR/tests/Net_Sieve", "tests/*")
