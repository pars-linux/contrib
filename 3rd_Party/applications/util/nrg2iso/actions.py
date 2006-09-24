#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools

def setup():
    pass

def build():
    autotools.make()

def install():
    pisitools.dobin("nrg2iso")
    pisitools.dodoc("CHANGELOG", "gpl.txt")
