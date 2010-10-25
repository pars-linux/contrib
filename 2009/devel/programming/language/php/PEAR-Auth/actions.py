#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="Auth-%s" % get.srcVERSION()

def install():
    pisitools.insinto("/usr/share/php5/PEAR", "Auth*")
    pisitools.insinto("/usr/share/php5/PEAR/tests/Auth", "tests/*")
    pisitools.insinto("/usr/share/php5/PEAR/doc/Auth", "README*")
    pisitools.insinto("/usr/share/php5/PEAR/doc/Auth/examples", "examples/*")
