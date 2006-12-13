#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="File_Passwd-1.1.6"

def install():
    pisitools.insinto("/usr/share/php5/PEAR/File", "Pass*")
    pisitools.insinto("/usr/share/php5/PEAR/tests/File_Passwd", "tests/*")