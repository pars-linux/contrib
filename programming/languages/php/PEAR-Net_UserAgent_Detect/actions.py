#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="Net_UserAgent_Detect-2.2.0"

def install():
    pisitools.insinto("/usr/share/php5/PEAR/Net/UserAgent", "Detect.php")
    pisitools.insinto("/usr/share/php5/PEAR/doc/Net_Useragent_Detect", "tests/example.php")