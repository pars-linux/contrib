#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="XML_Serializer-0.18.0"

def install():
    items = ['Serializer.php', 'Unserializer.php']
    for item in items:
        pisitools.insinto("/usr/share/php5/PEAR/XML", item)
    pisitools.insinto("/usr/share/php5/PEAR/XML/doc","doc/*")
    pisitools.insinto("/usr/share/php5/PEAR/XML/examples","examples/*")