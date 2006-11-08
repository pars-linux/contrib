#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="System_Command-1.0.5"

def install():
    pisitools.insinto("/usr/share/php5/PEAR/System","Command.php")