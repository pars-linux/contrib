#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="SOAP-0.9.4"

def install():
    pisitools.insinto("/usr/share/php5/PEAR/SOAP/Server", "Server/*")
    pisitools.insinto("/usr/share/php5/PEAR/SOAP/Transport", "Transport/*")
    pisitools.insinto("/usr/share/php5/PEAR/SOAP/tools", "tools/*")
    pisitools.insinto("/usr/share/php5/PEAR/SOAP/Type", "Type/*")
    pisitools.insinto("/usr/share/php5/PEAR/doc/SOAP", "example/*")
    items = ['Base.php', 'Value.php', 'Client.php', 'Fault.php', 'Server.php', 'Transport.php', 'WSDL.php', 'Disco.php', 'Parser.php']
    for item in items:
        pisitools.insinto("/usr/share/php5/PEAR/SOAP", item)