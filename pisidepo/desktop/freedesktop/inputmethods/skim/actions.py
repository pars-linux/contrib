#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Rajeev J Sebastian <rajeev@rachanamalayalam.org>

from pisi.actionsapi import scons
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    scons.make("configure prefix=/usr/kde/3.5" )

def build():
    scons.make( )

def install():
    scons.install(argument="DESTDIR")
    pisitools.dodoc("ChangeLog", "AUTHORS", "INSTALL*", "NEWS", "README*")

