#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="XML_Serializer-%s" % get.srcVERSION()

def install():
    pisitools.insinto("/usr/share/php5/PEAR/XML", "XML/*")
    pisitools.insinto("/usr/share/php5/PEAR/doc/XML_Serializer","doc/*")
    pisitools.insinto("/usr/share/php5/PEAR/doc/XML_Serializer/examples","examples/*")
    pisitools.insinto("/usr/share/php5/PEAR/tests/XML_Serializer", "tests/*")
