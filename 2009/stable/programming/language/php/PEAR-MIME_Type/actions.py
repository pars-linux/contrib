#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="MIME_Type-%s" % get.srcVERSION()

def install():
    pisitools.insinto("/usr/share/php5/PEAR/MIME","MIME/Type.php")
    pisitools.insinto("/usr/share/php5/PEAR/MIME/Type","MIME/Type/Parameter.php")
    pisitools.insinto("/usr/share/php5/PEAR/MIME/Type","MIME/Type/Extension.php")
    pisitools.insinto("/usr/share/php5/PEAR/docs/MIME_Type", "docs/examples/example.php")
