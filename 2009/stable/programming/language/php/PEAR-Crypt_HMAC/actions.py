#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="Crypt_HMAC-%s" % get.srcVERSION()

def install():
    pisitools.insinto("/usr/share/php5/PEAR/Crypt", "HMAC.php")
    pisitools.insinto("/usr/share/php5/PEAR/tests/Crypt_HMAC", "tests/*")
