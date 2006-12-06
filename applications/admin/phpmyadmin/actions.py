#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="phpMyAdmin-2.8.2"

def install():
    pisitools.dodir("/var/www/localhost/htdocs/phpmyadmin")
    shelltools.move("%s/phpMyAdmin-2.8.2" % get.workDIR(),"%s/var/www/localhost/htdocs/phpmyadmin" % get.installDIR())
