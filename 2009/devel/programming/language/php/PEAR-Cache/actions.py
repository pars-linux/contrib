#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="Cache-%s" % get.srcVERSION()


def install():
    pisitools.insinto("/usr/share/php5/PEAR", "Cache.php")
    pisitools.insinto("/usr/share/php5/PEAR/Cache/Container", "Container/*")
    items = ['Application.php', 'Container.php', 'Graphics.php', 'Output.php', 'Error.php', 'HTTP_Request.php', 'Function.php', 'OutputCompression.php']
    for item in items:
        pisitools.insinto("/usr/share/php5/PEAR/Cache", "%s" % item)
