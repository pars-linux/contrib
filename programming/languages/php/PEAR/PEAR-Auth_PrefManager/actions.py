#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="Auth_PrefManager-1.1.4"

def install():
    pisitools.insinto("/usr/share/php5/PEAR/Auth", "PrefManager.php")
    pisitools.insinto("/usr/share/php5/PEAR/doc/Auth_PrefManager", "docs/*")