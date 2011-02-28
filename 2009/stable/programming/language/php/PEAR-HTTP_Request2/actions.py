#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

WorkDir="HTTP_Request2-2.0.0beta1"
pear="/usr/share/php5/PEAR"

def install():
    pisitools.insinto("%s/HTTP" % pear, "Request2*")
    pisitools.insinto("%s/doc/HTTP_Request2" % pear, "docs/*")
    pisitools.insinto("%s/tests/HTTP_Request2" % pear, "tests/*")
