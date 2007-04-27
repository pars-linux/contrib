#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="Net_URL-1.0.14"

def install():
    pisitools.insinto("/usr/share/php5/PEAR/Net", "URL.php")
    pisitools.insinto("/usr/share/php5/PEAR/doc/Net_URL", "docs/*")