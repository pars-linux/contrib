#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="Log-1.9.9"

def install():
    pisitools.insinto("/usr/share/php5/PEAR", "Log*")
    pisitools.insinto("/usr/share/php5/PEAR/misc", "misc/*")
    pisitools.insinto("/usr/share/php5/PEAR/doc/Log", "docs/*")
    pisitools.insinto("/usr/share/php5/PEAR/tests/Log", "tests/*")