#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="Net_POP3-1.3.6"

def install():
    pisitools.insinto("/usr/share/php5/PEAR/Net", "POP3.php")
    pisitools.insinto("/usr/share/php5/PEAR/doc/Net_POP3", "Net_POP3_example.php")