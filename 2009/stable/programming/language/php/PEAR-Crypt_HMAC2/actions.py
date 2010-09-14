#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="Crypt_HMAC2-%s" % get.srcVERSION()
pear="/usr/share/php5/PEAR/"

def install():
    pisitools.insinto("%s/Crypt" % pear, "Crypt/HMAC2*")
    pisitools.insinto("%s/tests/Crypt_HMAC2" % pear, "tests/*")
    pisitools.insinto("%s/doc/Crypt_HMAC2" % pear, "docs/*")
