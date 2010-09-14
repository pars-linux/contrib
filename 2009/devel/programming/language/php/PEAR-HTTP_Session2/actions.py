#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="HTTP_Session2-%s" % get.srcVERSION()
pear="/usr/share/php5/PEAR"

def install():
    pisitools.insinto("%s/HTTP" % pear, "HTTP/Session2*")
    pisitools.insinto("%s/doc/HTTP_Session2" % pear, "docs/*")
    pisitools.insinto("%s/tests/HTTP_Session2" % pear, "tests/*")
