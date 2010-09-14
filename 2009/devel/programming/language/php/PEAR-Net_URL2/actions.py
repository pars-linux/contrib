#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="Net_URL2-%s" % get.srcVERSION()
pear="/usr/share/php5/PEAR"

def install():
    pisitools.insinto("%s/Net" % pear, "URL2.php")
    pisitools.insinto("%s/doc/Net_URL2" % pear, "docs/*")
