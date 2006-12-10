#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="HTTP_Client-1.1.0"

def install():
    pisitools.insinto("/usr/share/php5/PEAR/HTTP", "Client*")
    pisitools.insinto("/usr/share/php5/PEAR/doc/HTTP_Client", "examples/*")
    # set permission
    shelltools.chmod("%s/usr/share/php5/PEAR/doc/HTTP_Client/link-checker.php" % get.installDIR())