#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="Net_FTP-1.3.2"

def install():
    pisitools.insinto("/usr/share/php5/PEAR/Net", "Net/*")
    pisitools.insinto("/usr/share/php5/PEAR/doc/Net_FTP", "example/*")