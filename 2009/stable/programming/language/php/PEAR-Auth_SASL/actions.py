#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="Auth_SASL-%s" % get.srcVERSION()

def install():
    pisitools.insinto("/usr/share/php5/PEAR/Auth", "Auth/SASL.php")
    pisitools.insinto("/usr/share/php5/PEAR/Auth/SASL", "Auth/SASL/*")
