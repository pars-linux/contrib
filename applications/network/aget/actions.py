#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def build():
    autotools.make()
    autotools.make("strip")

def install():
    autotools.install()
    pisitools.dobin("aget")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "INSTALL", "README*", "THANKS", "TODO")