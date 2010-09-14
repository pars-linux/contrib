#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.tx

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="HTML_QuickForm2-%s" % get.srcVERSION()
pear="/usr/share/php5/PEAR"

def install():
    pisitools.insinto("%s/HTML" % pear, "HTML/QuickForm*")
    pisitools.insinto("%s/doc/HTML_QuickForm2" % pear, "docs/*")
    pisitools.insinto("%s/tests/HTML_QuickForm2" % pear, "tests/*")
