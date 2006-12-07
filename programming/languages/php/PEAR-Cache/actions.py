#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="Cache-1.5.5RC4"

def install():
    pisitools.insinto("/usr/share/php5/PEAR", "Cache.php")
    pisitools.insinto("/usr/share/php5/PEAR/Cache/Container", "Container/*")
    items = ['Application.php', 'Container.php', 'Graphics.php', 'Output.php', 'Error.php', 'HTTP_Request.php', 'Function.php', 'OutputCompression.php']
    for item in items:
        pisitools.insinto("/usr/share/php5/PEAR/Cache", "%s" % item)