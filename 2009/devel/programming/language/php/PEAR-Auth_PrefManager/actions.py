#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="Auth_PrefManager-%s" % get.srcVERSION()

def install():
    pisitools.insinto("/usr/share/php5/PEAR/Auth", "PrefManager.php")
    pisitools.insinto("/usr/share/php5/PEAR/doc/Auth_PrefManager", "docs/*")
    pisitools.insinto("/usr/share/php5/PEAR/tests/Auth_PrefManager", "tests/*")
