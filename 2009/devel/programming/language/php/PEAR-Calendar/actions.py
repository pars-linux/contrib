#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="Calendar-%s" % get.srcVERSION()

def install():
    pisitools.insinto("/usr/share/php5/PEAR/Calendar", "*.php")
    pisitools.insinto("/usr/share/php5/PEAR/Calendar/Decorator", "Decorator/*")
    pisitools.insinto("/usr/share/php5/PEAR/Calendar/Engine", "Engine/*")
    pisitools.insinto("/usr/share/php5/PEAR/Calendar/Month", "Month/*")
    pisitools.insinto("/usr/share/php5/PEAR/Calendar/Util", "Util/*")
    pisitools.insinto("/usr/share/php5/PEAR/Calendar/Table", "Table/*")
    pisitools.insinto("/usr/share/php5/PEAR/doc/Calendar", "docs/*")
    pisitools.insinto("/usr/share/php5/PEAR/tests/Calendar", "tests/*")
