#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="MDB2_Driver_oci8-1.3.0"

def install():
    pisitools.insinto("/usr/share/php5/PEAR/MDB2/Driver", "MDB2/Driver/*")