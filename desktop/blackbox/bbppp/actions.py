#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = "bbppp-0.2.3"

def setup():
    autotools.configure()
def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("README", "COPYING", "AUTHORS", "BUGS", "INSTALL", "ChangeLog", "NEWS", "TODO", "data/README.bbppp")