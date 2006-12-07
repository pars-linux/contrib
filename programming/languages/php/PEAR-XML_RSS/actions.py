#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="XML_RSS-0.9.10"

def install():
    pisitools.insinto("/usr/share/php5/PEAR/XML", "RSS.php")
    pisitools.insinto("/usr/share/php5/PEAR/tests/XML_RSS", "tests/*")