#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 Rajeev J Sebastian, rajeev.sebastian@gmail.com
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("AUTHORS", "ChangeLog", "INSTALL", "NEWS", "README")
