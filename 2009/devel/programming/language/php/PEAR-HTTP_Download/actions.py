#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="HTTP_Download-%s" % get.srcVERSION()

def install():
    pisitools.insinto("/usr/share/php5/PEAR/HTTP", "HTTP/Download*")
    pisitools.insinto("/usr/share/php5/PEAR/tests/HTTP_Download", "tests/*")
    pisitools.dodoc("LICENSE")
