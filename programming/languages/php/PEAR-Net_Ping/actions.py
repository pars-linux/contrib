#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="Net_Ping-2.4.1"

def install():
    pisitools.insinto("/usr/share/php5/PEAR/Net", "Ping.php")
    pisitools.insinto("/usr/share/php5/PEAR/doc/Net_Ping", "docs/examples/example.php")
    pisitools.insinto("/usr/share/php5/PEAR/tests/Net_Ping", "tests/*")