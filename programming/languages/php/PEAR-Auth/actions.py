#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="Auth-1.4.3"

def install():
    pisitools.insinto("/usr/share/php5/PEAR", "Auth.php")
    pisitools.insinto("/usr/share/php5/PEAR/Auth", "Container.php")
    pisitools.insinto("/usr/share/php5/PEAR/Auth", "Auth/*")
    pisitools.insinto("/usr/share/php5/PEAR/Auth/Container", "Container/*")
    pisitools.insinto("/usr/share/php5/PEAR/Auth/Frontend", "Frontend/*")
    pisitools.insinto("/usr/share/php5/PEAR/tests/Auth", "tests/*")
    pisitools.insinto("/usr/share/php5/PEAR/doc/Auth", "README.Auth")