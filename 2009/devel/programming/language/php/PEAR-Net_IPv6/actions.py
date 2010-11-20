#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="Net_IPv6-1.2.0b"

def install():
    pisitools.insinto("/usr/share/php5/PEAR/Net", "Net/IPv6.php")
    pisitools.insinto("/usr/share/php5/PEAR/tests/Net_IPv6","tests/*")
