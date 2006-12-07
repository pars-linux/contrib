#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="Auth_HTTP-2.1.6"

def install():
    pisitools.insinto("/usr/share/php5/PEAR/Auth", "Auth_HTTP.php", "HTTP.php")
    pisitools.insinto("/usr/share/php5/PEAR/tests/Auth_HTTP", "tests/*")