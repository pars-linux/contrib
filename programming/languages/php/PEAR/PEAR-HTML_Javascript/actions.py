#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="HTML_Javascript-1.1.1"

def install():
    pisitools.insinto("/usr/share/php5/PEAR/HTML", "Javascript*")
    pisitools.insinto("/usr/share/php5/PEAR/doc/HTML_Javascript", "examples/*")
    pisitools.insinto("/usr/share/php5/PEAR/tests/HTML_Javascript", "tests/*")