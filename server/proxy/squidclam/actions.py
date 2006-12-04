#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    shelltools.cd("src")
    autotools.make()

def install():
    pisitools.dobin("src/squidclam")
    pisitools.insinto("/etc", "sample.conf", "squidclam.conf")
    pisitools.dodoc("antivir.php", "README", "Changelog", "TODO", "sample.conf")
