#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="MDB2_Driver_mysqli-1.5.0b2"

def install():
    pisitools.insinto("/usr/share/php5/PEAR/MDB2/Driver", "MDB2/Driver/*")
    pisitools.insinto("/usr/share/php5/PEAR/tests/MDB2_Driver_mysqli", "tests/*")
