#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir ="hk_classes-0.8.3"
def setup():
    autotools.configure("--with-mysql \
                         --with-postgres \
                         --with-odbc")
def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README")
    pisitools.dohtml("documentation/tutorial/*")
