#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="Pager-2.4.3"

def install():
    items = ['Common.php', 'HtmlWidgets.php', 'Pager.php', 'Sliding.php', 'Jumping.php', 'Pager_savebc.php']
    for item in items:
        pisitools.insinto("/usr/share/php5/PEAR/Pager", item)
    pisitools.insinto("/usr/share/php5/PEAR/doc/Pager", "examples/*")
    pisitools.insinto("/usr/share/php5/PEAR/tests/Pager", "tests/*")