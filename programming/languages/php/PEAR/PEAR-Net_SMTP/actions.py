#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="Net_SMTP-%s" % get.srcVERSION()

def install():
    pisitools.insinto("/usr/share/php5/PEAR/Net", "SMTP.php")
    pisitools.insinto("/usr/share/php5/PEAR/doc/Net_SMTP", "docs/*")
    pisitools.insinto("/usr/share/php5/PEAR/tests/Net_SMTP", "tests/*")
