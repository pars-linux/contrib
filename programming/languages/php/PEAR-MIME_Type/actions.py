#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="MIME_Type-1.0.0"

def install():
    pisitools.insinto("/usr/share/php5/PEAR/MIME","Type.php")
    pisitools.insinto("/usr/share/php5/PEAR/MIME/Type","Parameter.php")
    pisitools.insinto("/usr/share/php5/PEAR/doc/MIME_Type","example.php")