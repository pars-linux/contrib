#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="Text_Diff-0.2.1"

def install():
    pisitools.insinto("/usr/share/php5/PEAR/Text", "Diff*")
    pisitools.insinto("/usr/share/php5/PEAR/doc/Text_Diff", "docs/*")
    pisitools.insinto("/usr/share/php5/PEAR/tests/Text_Diff", "tests/*")