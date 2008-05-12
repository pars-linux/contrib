#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="HTTP_WebDAV_Server-1.0.0RC4"

def install():
    pisitools.insinto("/usr/share/php5/PEAR/HTTP/WebDAV", "Server*")
    pisitools.insinto("/usr/share/php5/PEAR/HTTP/WebDAV/Tools", "Tools/*")
    pisitools.insinto("/usr/share/php5/PEAR/HTTP/WebDAV/db", "db/*")
    pisitools.insinto("/usr/share/php5/PEAR/HTTP/WebDAV", "dav.txt")
    pisitools.insinto("/usr/share/php5/PEAR/doc/HTTP_WebDAV_Server", "README")