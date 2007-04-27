#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="HTML_Common2-0.3.0"

def install():
    pisitools.insinto("/usr/share/php5/PEAR/HTML", "Common2.php")
    pisitools.insinto("/usr/share/php5/PEAR/tests/HTML_Common2", "tests/*")