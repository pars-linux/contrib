#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="Crypt_CHAP-1.0.0"

def install():
    pisitools.insinto("/usr/share/php5/PEAR/Crypt", "CHAP.php")
    pisitools.insinto("/usr/share/php5/PEAR/tests/Crypt_CHAP", "tests/*")