#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="XML_Parser-1.2.7"

def install():
    pisitools.insinto("/usr/share/php5/PEAR/XML","Parser.php")
    pisitools.insinto("/usr/share/php5/PEAR/XML/Parser","Parser/Simple.php")
    pisitools.insinto("/usr/share/php5/PEAR/XML/examples","examples/*")
    pisitools.insinto("/usr/share/php5/PEAR/XML/tests","tests/*")