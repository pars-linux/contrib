#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="HTTP_Upload-0.9.1"

def install():
    pisitools.insinto("/usr/share/php5/PEAR/HTTP", "Upload.php")
    pisitools.insinto("/usr/share/php5/PEAR/doc/HTTP_Upload", "docs/upload_example.php")